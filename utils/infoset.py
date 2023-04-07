from typing import Callable

from typing_extensions import Self

from .card import Card, Rank, Suit
from .player import Player
from .team import Team


class InfoSet:
    def __init__(self: Self, **kwargs) -> None:
        # trump rank and suit
        self.trump_rank: Rank = None
        self.trump_suit: Suit = None

        # play sequence of cards this round
        self.round_play_seq: list[list[Card]] = []

        # history of all plays for the entire game
        self.game_play_seq: list[list[Card]] = []

        # list of the teams in the game
        self.teams: list[Team] = []

        # list of the players in the game, should alternate between teams
        self.players: list[Player] = []

        # list of bank cards
        self.bank_cards: list[Card] = []

        # index of current player
        self.cur_player_idx: int = 0

        # index of starting player
        self.starting_player_idx: int = 0

        for key, val in kwargs.items():
            if key in self.__dict__:
                self.__dict__[key] = val

    
    
    @property
    def num_players(self: Self) -> int:
        return len(self.players)

    @property
    def current_player(self: Self) -> Player:
        return self.players[self.cur_player_idx]

    @property
    def starting_player(self: Self) -> Player:
        return self.players[self.starting_player_idx]

    def __str__(self: Self) -> None:
        format_players: Callable[..., str] = (
            lambda p: "[" + ",".join(f"\n\t\t{i}" for i in p) + "\n\t]"
        )
        return "Infoset:" + "".join(
            f"\n\t{k} = {v if k != 'players' else format_players(v)}"
            for k, v in self.__dict__.items()
        )

    __repr__: Callable[..., str] = __str__
