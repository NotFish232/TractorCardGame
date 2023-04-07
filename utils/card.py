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


class Suit(Enum):
    Hearts = 0
    Diamonds = 1
    Clubs = 2
    Spades = 3


suit_to_symbol: dict[Suit, str] = {
    Suit.Hearts: "♥",
    Suit.Diamonds: "♦",
    Suit.Clubs: "♣",
    Suit.Spades: "♠",
}


@total_ordering
class Card:
    def __init__(self: Self, *, rank: Rank, suit: Suit = None) -> None:
        if rank != Rank.BlackJoker and rank != Rank.RedJoker:
            assert suit is not None, "Suit must be provided for non-joker cards"

        if rank == Rank.BlackJoker or rank == Rank.RedJoker:
            assert suit is None, "Suit can not be provided for jokersF"

        self.rank: Rank = rank
        self.suit: Suit = suit

    def __eq__(self: Self, other: object) -> bool:
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit

        raise NotImplementedError("Comparison only supported with other card objects")

    def __lt__(self: Self, other: object) -> bool:
        if isinstance(other, Card):
            return self.rank < other.rank

        raise NotImplementedError("Comparision only supported with other card objects")

    def __str__(self: Self) -> str:
        if self.rank == Rank.RedJoker:
            return "Red Joker"
        if self.rank == Rank.BlackJoker:
            return "Black Joker"

        return f"{self.rank.name} of {self.suit.name}"

    def __repr__(self: Self) -> str:
        if self.rank == Rank.RedJoker:
            return "rJoker"
        if self.rank == Rank.BlackJoker:
            return "bJoker"

        suit_symbol: str = suit_to_symbol[self.suit]

        return f"{self.rank.value if self.rank.value <= 10 else self.rank.name[0]}{suit_symbol}"
