from ..card import Card, Rank, Suit
from ..infoset import InfoSet
from .card_utils import *


def find_round_winner(infoset: InfoSet) -> int:
    pass


def follows_pattern(move: list[Card], first_move: list[Card]) -> bool:
    pass


def can_follow_suit(hand: list[Card], first_move: list[Card]) -> bool:
    return sum(1 for card in hand if card.suit == first_move[0].suit) >= len(first_move)


def follows_suit(move: list[Card], first_move: list[Card]) -> bool:
    pass


def is_move_valid(move: list[Card], infoset: InfoSet) -> bool:
    """
    move should be a sorted list of cards
    """
    if len(move) == 0:
        return False

    if len(infoset.round_play_seq) == 0:
        return is_first_move_valid(move, infoset)

    first_move: list[Card] = infoset.round_play_seq[0]
    hand: list[Card] = infoset.current_player.cards

    if can_follow_suit(hand, first_move):
        if not follows_suit(move, first_move):
            return False


def is_first_move_valid(move: list[Card], infoset: InfoSet) -> bool:
    if len(move) == 1:
        return True
    # either no trumps or entire move is trumps
    if 0 < sum(1 for card in move if is_trump(card)) < len(move):
        return False
    # check if all cards all the same suite
    if not all(card.suit == move[0].suit for card in move):
        return False

    if len(move) % 2 == 0:
        for i in range(0, len(move), 2):
            if move[i] != move[i + 1]:
                return False


def _test() -> None:
    pass


if __name__ == "__main__":
    _test()
