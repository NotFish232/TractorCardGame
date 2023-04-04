from utils.card import Card, Rank, Suit
from utils.infoset import InfoSet


def sort_cards(cards: list[Card], infoset: InfoSet) -> None:
    """
    sort cards based on trump rank and trump suit in infoset
    """
    # hacky but it works
    def _sorting_key(c: Card) -> int:
        if c.rank == infoset.trump_rank:
            if c.suit == infoset.trump_suit:
                return 29
            return 28

        if c.suit == infoset.trump_suit:
            return c.rank.value + 13

        return c.rank.value

    cards.sort(key=_sorting_key, reverse=True)


def is_trump(card: Card, infoset: InfoSet) -> bool:
    return (
        card.rank == Rank.RedJoker
        or card.rank == Rank.BlackJoker
        or card.suit == infoset.trump_suit
        or card.rank == infoset.trump_rank
    )


def is_consecutive(card1: Card, card2: Card, infoset: InfoSet) -> bool:
    if card2.rank == Rank.RedJoker:
        return card1.rank == Rank.BlackJoker
    
    if card2.rank == Rank.BlackJoker:
        return card1.rank == infoset.trump_rank and card1.suit == infoset.trump_suit
    
    if card2.rank == infoset.trump_rank:
        if card2.suit == infoset.trump_suit:
            return card1.rank == infoset.trump_rank and card1.suit != infoset.trump_suit
        return card1.rank == Rank.Ace and card1.suit == infoset.trump_suit
    
    if card2.rank == Rank.Two:
        return False
    
    if card2.rank.value == infoset.trump_rank.value + 1:
        return card2.rank.value == card1.rank.value + 2
    
    return card2.rank.value == card1.rank.value + 1
    
    


def is_single_higher(card1: Card, card2: Card, infoset: InfoSet):
    if card1.rank == Rank.RedJoker:
        return True
    if card2.rank == Rank.RedJoker:
        return False
    if card1.rank == Rank.BlackJoker:
        return True
    if card2.rank == Rank.BlackJoker:
        return False

    if card1.suit == infoset.trump_suit and card1.rank == infoset.trump_rank:
        return True

    if card2.suit == infoset.trump_suit and card2.rank == infoset.trump_rank:
        return False

    if card1.rank == infoset.trump_rank:
        return True
    if card2.rank == infoset.trump_rank:
        return False

    if card1.suit == infoset.trump_suit:
        if card2.suit == infoset.trump_suit:
            return card1 > card2
        return True

    if card2.suit == infoset.trump_suit:
        return False

    return card1 > card2


def is_higher(cards1: list[Card], cards2: list[Card], infoset: InfoSet) -> bool:
    assert len(cards1) == len(cards2) != 0

    if len(cards1) == 1:
        return is_single_higher(cards1[0], cards2[0], infoset)

def _test_consecutive() -> None:
    pass
def _test() -> None:
    pass

if __name__ == "__main__":
    _test()