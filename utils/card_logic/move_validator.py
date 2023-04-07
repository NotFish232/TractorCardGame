from ..card import Card, Rank, Suit
from ..infoset import InfoSet
from .card_utils import *
from .pattern import Pattern, PatternType


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

    if len(move) != len(first_move):
        return False

    first_move_pattern: Pattern = Pattern(first_move, infoset)
    move_pattern: Pattern = Pattern(move, infoset)

    if is_trump(first_move[0], infoset):
        hand_trumps: list[Card] = get_trumps(hand, infoset)
        move_trump_count: int = get_trump_count(move, infoset)

        # pattern doesnt matter here as long as using all trumps in hand
        # if you are not using all your suits, and your using less than first_move: False
        if move_trump_count == len(hand_trumps):
            return True
        elif move_trump_count < len(first_move):
            return False

        hand_pattern: Pattern = Pattern(hand_trumps, infoset)
    else:
        suit: Suit = first_move[0].suit
        hand_suits: list[Card] = get_suits(hand, suit, infoset)
        move_suit_count: int = get_suit_count(move, suit, infoset)

        # pattern doesnt matter here as long as using all suits in hand
        # if you are not using all your suits, and your using less than first_move: False
        if move_suit_count == len(hand_suits):
            return True
        elif move_suit_count < len(first_move):
            return False

        hand_pattern: Pattern = Pattern(hand_suits, infoset)

    # if any frequency is better represented in hand than the move
    num_cards: int = 0
    for freq, cards in sorted(first_move_pattern.card_groups.items(), reverse=True):
        first_move_count: int = len(cards)
        move_count: int = len(move_pattern.card_groups.get(freq, []))
        hand_count: int = len(hand_pattern.card_groups.get(freq, []))

        if (
            hand_count > move_count
            and move_count != first_move_count
            and num_cards + freq * hand_count <= len(move)
        ):
            return False

        num_cards += freq * move_count

    return True


def is_first_move_valid(move: list[Card], infoset: InfoSet) -> bool:
    if len(move) == 1:
        return True
    # either no trumps or entire move is trumps
    if 0 < sum(1 for card in move if is_trump(card, infoset)) < len(move):
        return False
    # check if all cards all the same suite
    if not all(card.suit == move[0].suit for card in move):
        return False

    return Pattern(move, infoset).type != PatternType.Unrecognized


def is_trump(card: Card, infoset: InfoSet) -> bool:
        return (
            card.rank == Rank.RedJoker
            or card.rank == Rank.BlackJoker
            or card.suit == infoset.trump_suit
            or card.rank == infoset.trump_rank
        )

def get_suits(cards: list[Card], suit: Suit, infoset: InfoSet) -> list[Card]:
    return [c for c in cards if c.suit == suit and not is_trump(c, infoset)]

def get_suit_count(cards: list[Card], suit: Suit, infoset: InfoSet) -> int:
    return len(get_suits(cards, suit, infoset))

def get_trumps(cards: list[Card], infoset: InfoSet) -> list[Card]:
    return [c for c in cards if is_trump(c, infoset)]

def get_trump_count(cards: list[Card], infoset: InfoSet) -> int:
    return len(get_trumps(cards, infoset))