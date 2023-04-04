from .card_utils import *
from utils.card import Card, Rank, Suit
from utils.infoset import InfoSet


def test_consecutive() -> None:
    infoset: InfoSet = InfoSet()
    infoset.trump_rank = Rank.Four
    infoset.trump_suit = Suit.Diamonds

    assert is_consecutive(
        Card(rank=Rank.Eight, suit=Suit.Clubs),
        Card(rank=Rank.Nine, suit=Suit.Clubs),
        infoset,
    )
    assert is_consecutive(
        Card(rank=Rank.Three, suit=Suit.Hearts),
        Card(rank=Rank.Five, suit=Suit.Hearts),
        infoset,
    )
    assert is_consecutive(
        Card(rank=Rank.Ace, suit=Suit.Diamonds),
        Card(rank=Rank.Four, suit=Suit.Spades),
        infoset,
    )
    assert is_consecutive(
        Card(rank=Rank.Four, suit=Suit.Hearts),
        Card(rank=Rank.Four, suit=Suit.Diamonds),
        infoset,
    )
    # fmt: off
    assert is_consecutive(
        Card(rank=Rank.Four, suit=Suit.Diamonds),
        Card(rank=Rank.BlackJoker),
        infoset
    )
    assert is_consecutive(
        Card(rank=Rank.BlackJoker),
        Card(rank=Rank.RedJoker),
        infoset
    )
    # fmt: on

    assert not is_consecutive(
        Card(rank=Rank.Five, suit=Suit.Spades),
        Card(rank=Rank.Seven, suit=Suit.Spades),
        infoset,
    )
    assert not is_consecutive(
        Card(rank=Rank.Four, suit=Suit.Hearts),
        Card(rank=Rank.Five, suit=Suit.Hearts),
        infoset,
    )
