from functools import total_ordering
from pathlib import Path
from typing import Callable

import arcade
from typing_extensions import Self

from game.utils.card import Card, Rank, Suit

ASSETS_FOLDER: str = Path(__file__).parent.parent / "assets/cards"
CARD_SCALE: float = 0.2
BORDER_WIDTH: int = 2


class CardSprite(arcade.Sprite):
    def __init__(self: Self, card: Card) -> None:
        filename: str = str(card).replace(" ", "_").lower() + ".png"
        super().__init__(ASSETS_FOLDER / filename, CARD_SCALE, hit_box_algorithm=None) 