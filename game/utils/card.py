from enum import Enum
from functools import total_ordering
from typing import Callable

from typing_extensions import Self


@total_ordering
class Rank(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14
    BlackJoker = 15
    RedJoker = 16

    def __lt__(self: Self, other: object) -> None:
        if isinstance(other, Rank):
            return self.value < other.value

        raise NotImplementedError("Comparison only supported between rank objects")


@total_ordering
class Suit(Enum):
    Spades = 1
    Clubs = 2
    Hearts = 3
    Diamonds = 4

    def __lt__(self: Self, other: object) -> None:
        if isinstance(other, Suit):
            return self.value < other.value

        raise NotImplementedError("Comparison only supported between suit objects")


class Card:
    def __init__(self: Self, *, rank: Rank, suit: Suit = None) -> None:
        if rank != Rank.BlackJoker and rank != Rank.RedJoker:
            assert suit is not None, "Suit must be provided for non-joker cards"

        if rank == Rank.BlackJoker or rank == Rank.RedJoker:
            assert suit is None, "Suit can not be provided for jokersF"

        self.rank: Rank = rank
        self.suit: Suit = suit

    def __hash__(self: Self) -> int:
        return hash((self.rank, self.suit))

    def __eq__(self: Self, other: object) -> bool:
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit

        raise NotImplementedError("Comparison only supported with other card objects")

    def __lt__(self: Self, other: object) -> bool:
        if isinstance(other, Card):
            return self.rank < other.rank

        raise NotImplementedError("Comparision only supported with other card objects")

    def __str__(self: Self) -> str:
        if self.rank == Rank.BlackJoker:
            return "Black Joker"
        if self.rank == Rank.RedJoker:
            return "Red Joker"

        return f"{self.rank.name} of {self.suit.name}"

    __repr__: Callable[..., str] = __str__
