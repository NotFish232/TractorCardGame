from utils.card import Card, Rank, Suit
from utils.infoset import InfoSet

from .pattern import Pattern


def get_round_winner(infoset: InfoSet) -> int:
    """
    returns index of round winner
    """
    highest_idx: int = infoset.starting_player_idx
    highest_pattern: Pattern = Pattern(infoset.round_play_seq[highest_idx], infoset)

    for i in range(1, len(infoset.round_play_seq)):
        idx: int = (infoset.starting_player_idx + i) % len(infoset.round_play_seq)
        pattern: Pattern = Pattern(infoset.round_play_seq[idx], infoset)

        # man I love operator overloading
        # check pattern for implementation
        if pattern > highest_pattern:
            highest_idx = idx
            highest_pattern = pattern

    return highest_idx


def get_round_pts(infoset: InfoSet) -> int:
    """
    returns the number of points in the round
    """
    pts: int = 0
    for move in infoset.round_play_seq:
        for card in move:
            if card.rank == Rank.Ten or card.rank == Rank.King:
                pts += 10
            if card.rank == Rank.Five:
                pts += 5
    return pts


def sort_cards(cards: list[Card], infoset: InfoSet) -> None:
    """
    sort cards based on trump rank and trump suit in infoset
    """

    # hacky but it works
    def _sorting_key(c: Card) -> int:
        if c.rank == Rank.RedJoker:
            return 100
        if c.rank == Rank.BlackJoker:
            return 99

        if c.rank == infoset.trump_rank:
            if c.suit == infoset.trump_suit:
                return 98
            return 94 + c.suit.value

        if c.suit == infoset.trump_suit:
            return c.rank.value + 52

        return c.rank.value + c.suit.value * 13

    cards.sort(key=_sorting_key, reverse=True)
