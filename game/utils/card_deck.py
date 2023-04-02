import random

from typing_extensions import Self

from ..sprites.card import Card, Rank, Suit


class CardDeck:
    def __init__(self: Self, *, num_card_decks: int = 3) -> None:
        self.cards: list[Card] = []
        self.num_card_decks: int = num_card_decks

        self.make_cards()

    def make_cards(self: Self) -> None:
        self.cards.clear()

        for rank in Rank:
            if rank == Rank.BlackJoker or rank == Rank.RedJoker:
                for _ in range(self.num_card_decks):
                    self.cards.append(Card(rank=rank, suit=None))

                continue

            for suit in Suit:
                for _ in range(self.num_card_decks):
                    self.cards.append(Card(rank=rank, suit=suit))

        random.shuffle(self.cards)

    def has_cards(self: Self) -> bool:
        return len(self.cards) > 0

    def deal_card(self: Self) -> Card:
        return self.cards.pop()

    def __len__(self: Self) -> str:
        return len(self.cards)

    def __str__(self: Self) -> str:
        return str(self.cards)
