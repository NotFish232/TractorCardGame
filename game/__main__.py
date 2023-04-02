from .tcg import TractorCardGame


def main() -> None:
    game: TractorCardGame = TractorCardGame()
    game.run()


if __name__ == "__main__":
    main()
