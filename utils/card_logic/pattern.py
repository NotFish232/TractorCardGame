from enum import Enum
from typing import Callable

from typing_extensions import Self

from utils.card import Card, Rank, Suit
from utils.infoset import InfoSet


class PatternType(Enum):
    Singles = 1
    ConsecutiveDoubles = 2
    ConsecutiveTriples = 3
    HighMisc = 5
    Unrecognized = 6


class Pattern:
    """
    classifies a move
    """

    def __init__(self: Self, cards: list[Card], infoset: InfoSet) -> None:
        self.infoset: InfoSet = infoset
        self.card_groups: dict[int, list[Card]] = self._make_freq_to_cards(cards)
        self.type: PatternType = self._classify_pattern()
        self.card_suits: dict[Suit | str, int] = self._classify_suits()

    def _check_high_misc(self: Self) -> PatternType:
        """
        returns high misc if it is high misc, otherwise, Unrecgonized
        """
        other_cards: list[Card] = self._get_remaining_cards()
        other_freq: dict[int, list[Card]] = self._make_freq_to_cards(other_cards)
        for freq, cards in self.card_groups.items():
            others: list[Card] = other_freq.get(freq, [])
            for card in cards:
                if any(self._is_higher(other, card) for other in others):
                    return PatternType.Unrecognized

        return PatternType.HighMisc

    def _classify_suits(self: Self) -> dict[Suit | str, int]:
        card_suits: dict[Suit | str, int] = {}

        for freq, cards in self.card_groups.items():
            for card in cards:
                if self._is_trump(card):
                    if "trump" not in card_suits:
                        card_suits["trump"] = 0
                    card_suits["trump"] += freq
                else:
                    if card.suit not in card_suits:
                        card_suits[card.suit] = 0
                    card_suits[card.suit] += freq

        return card_suits

    def _classify_pattern(self: Self) -> PatternType:
        if len(self.card_groups.keys()) == 1:
            freq: int = next(iter(self.card_groups.keys()))
            cards: list[Card] = self.card_groups[freq]

            if freq == 1:
                if len(cards) == 1:
                    return PatternType.Singles
                return self._check_high_misc()

            if not self._is_consecutive_series(cards):
                return PatternType.Unrecognized

            assert 2 <= freq <= 3

            return PatternType(freq)

        return self._check_high_misc()

    def __eq__(self: Self, other: object) -> bool:
        if isinstance(other, Pattern):
            # check that in the same suit
            if self.card_suits.keys() != other.card_suits.keys():
                return False

            # check that same freqs, each freq has the same number of cards
            if self.card_groups.keys() != other.card_groups.keys():
                return False
            
            return all(
                len(c1) == len(c2)
                for c1, c2 in zip(self.card_groups.values(), other.card_groups.values())
            )

        raise NotImplementedError()

    def __gt__(self: Self, other: object) -> bool:
        if isinstance(other, Pattern):
            # seems really weird check equality inside >, but equality only checks that the patterns are the same
            if self != other:
                return False

            for freq in self.card_groups.keys():
                for c1, c2 in zip(self.card_groups[freq], other.card_groups[freq]):
                    if not self._is_higher(c1, c2):
                        return False

            return True

        raise NotImplementedError()

    def __str__(self: Self) -> str:
        pass

    def _is_consecutive(self: Self, card1: Card, card2: Card) -> bool:
        if card2.rank == Rank.RedJoker:
            return card1.rank == Rank.BlackJoker

        if card2.rank == Rank.BlackJoker:
            return (
                card1.rank == self.infoset.trump_rank
                and card1.suit == self.infoset.trump_suit
            )

        if card2.rank == self.infoset.trump_rank:
            if card2.suit == self.infoset.trump_suit:
                return (
                    card1.rank == self.infoset.trump_rank
                    and card1.suit != self.infoset.trump_suit
                )
            return card1.rank == Rank.Ace and card1.suit == self.infoset.trump_suit

        if card2.rank == Rank.Two:
            return False

        if card2.rank.value == self.infoset.trump_rank.value + 1:
            return card2.rank.value == card1.rank.value + 2

        return card2.rank.value == card1.rank.value + 1

    def _is_consecutive_series(self: Self, cards: list[Card]) -> bool:
        for i in range(len(cards) - 1):
            if not self.is_consecutive(cards[i], cards[i + 1]):
                return False
        return True

    def _get_remaining_cards(self: Self) -> list[Card]:
        """
        returns all cards you don't know about
        this is hidden information
        used to figure out whether high values are allowed
        """
        remaining_cards: list[Card] = []

        for player in self.infoset.players:
            if player == self.infoset.current_player:
                continue

            remaining_cards.extend(player.cards)

        if not self.infoset.current_player.is_banker:
            remaining_cards.extend(self.infoset.bank_cards)

        return remaining_cards

    def _make_freq_to_cards(self: Self, cards: list[Card]) -> dict[int, list[Card]]:
        """
        maps frequency to cards
        """
        freq_to_card: dict[int, list[Card]] = {}

        i = 0
        while i < len(cards):
            count = 1

            while i < len(cards) - 1 and cards[i] == cards[i + 1]:
                count += 1
                i += 1

            if count not in freq_to_card:
                freq_to_card[count] = []
            freq_to_card[count].append(cards[i])

            i += 1

        return freq_to_card

    def _is_trump(self: Self, card: Card) -> bool:
        return (
            card.rank == Rank.RedJoker
            or card.rank == Rank.BlackJoker
            or card.suit == self.infoset.trump_suit
            or card.rank == self.infoset.trump_rank
        )

    def _is_higher(self: Self, card1: Card, card2: Card):
        if card1.rank == Rank.RedJoker:
            return True
        if card2.rank == Rank.RedJoker:
            return False
        if card1.rank == Rank.BlackJoker:
            return True
        if card2.rank == Rank.BlackJoker:
            return False

        if (
            card1.suit == self.infoset.trump_suit
            and card1.rank == self.infoset.trump_rank
        ):
            return True

        if (
            card2.suit == self.infoset.trump_suit
            and card2.rank == self.infoset.trump_rank
        ):
            return False

        if card1.rank == self.infoset.trump_rank:
            return True
        if card2.rank == self.infoset.trump_rank:
            return False

        if card1.suit == self.infoset.trump_suit:
            if card2.suit == self.infoset.trump_suit:
                return card1 > card2
            return True

        if card2.suit == self.infoset.trump_suit:
            return False

        return card1 > card2
