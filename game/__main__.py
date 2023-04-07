from utils.card import Card
from utils.infoset import InfoSet

from . import TractorCardGame


def random_predictor(infoset: InfoSet) -> list[Card]:
    return [infoset.current_player.cards.pop()]


def main() -> None:
    game: TractorCardGame = TractorCardGame(predictors=[None] * 6)
    game.run()


if __name__ == "__main__":
    main()
