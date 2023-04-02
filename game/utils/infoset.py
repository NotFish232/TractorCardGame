from typing import Callable

from typing_extensions import Self

from .card import Card, Rank, Suit
from .player import Player
from .team import Team


class InfoSet:
    def __init__(self: Self) -> None:
        # trump rank and suit
        self.trump_rank: Rank = None
        self.trump_suit: Suit = None

        # play sequence of cards this round
        self.round_play_seq: list[tuple[Card]] = []

        # history of all plays for the entire game
        self.history_play_seq: list[tuple[Card]] = []

        # list of the teams in the game
        self.teams: list[Team] = []

        # list of the players in the game, should alternate between teams
        self.players: list[Player] = []

        # list of bank cards
        self.bank_cards: list[Card] = []

    def __str__(self: Self) -> None:
        return "Infoset: " + "".join(f"\n\t{k} = {v}" for k, v in self.__dict__.items())

    __repr__: Callable[..., str] = __str__
