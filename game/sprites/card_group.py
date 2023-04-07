import math
from pathlib import Path

import arcade
from typing_extensions import Self

from utils.card import Card

ASSETS_FOLDER: str = Path(__file__).parent.parent / "assets/cards"
CARD_SCALE: float = 0.2

# distance between each card horiziontally
CARD_SPACING: int = 40

# distance to raise card when selecting
SELECT_CARD_DIST: int = 20

"""
Represents a group of cards for drawing
Wrapper around a SpriteList
"""


class CardGroup:
    def __init__(
        self: Self,
        cards: list[Card],
        x_position: float = None,
        y_position: float = None,
        *,
        rotation: float = 0,
        size: int = 1
    ) -> None:

        self.sprite_list: arcade.SpriteList = arcade.SpriteList()
        self.rotation: float = rotation
        self.selected_cards = []

        for card in cards:
            filename: str = self.card_to_filename(card)
            sprite: arcade.Sprite = arcade.Sprite(
                ASSETS_FOLDER / filename, size * CARD_SCALE
            )
            self.sprite_list.append(sprite)

        if x_position is not None and y_position is not None:
            self.set_position(x_position, y_position)

    def set_position(
        self: Self, x_position: float, y_position: float, rotation: float = None
    ) -> None:
        self.x_position: float = x_position
        self.y_position: float = y_position

        if rotation is not None:
            self.rotation = rotation

        offset: float = CARD_SPACING * (len(self.sprite_list) - 1) / 2
        x_offset: float = x_position - offset * math.cos(self.rotation)
        y_offset: float = y_position - offset * math.sin(self.rotation)

        for i, sprite in enumerate(self.sprite_list):
            sprite.set_position(
                x_offset + i * CARD_SPACING * math.cos(self.rotation),
                y_offset + i * CARD_SPACING * math.sin(self.rotation),
            )
            sprite.angle = math.degrees(self.rotation)

    def card_to_filename(self: Self, card: Card) -> None:
        return str(card).replace(" ", "_").lower() + ".png"

    def toggle_state(self: Self, sprite: arcade.Sprite, state: bool) -> None:
        sprite.set_position(
            sprite.center_x, sprite.center_y + (1 if state else -1) * SELECT_CARD_DIST
        )

    def mouse_click(self: Self, x: int, y: int) -> None:

        # iterate backwards to prevent weird overlapping
        for i in range(len(self.sprite_list) - 1, -1, -1):
            sprite: arcade.Sprite = self.sprite_list[i]

            if sprite.collides_with_point((x, y)):

                if i in self.selected_cards:
                    self.selected_cards.remove(i)
                    self.toggle_state(sprite, False)
                else:
                    self.selected_cards.append(i)
                    self.toggle_state(sprite, True)

                # only intersect with first clicked sprite
                break

    """
    Indexes are sorted in reverse order 
    """

    def get_selected_card_idxs(
        self: Self, clear_selected: bool = True, clear_sprites: bool = True
    ) -> list[int]:
        idxs: list[int] = sorted(self.selected_cards, reverse=True)

        if clear_sprites:
            for idx in idxs:
                self.sprite_list.pop(idx)

            self.set_position(self.x_position, self.y_position)

        if clear_selected:
            self.selected_cards.clear()

        return idxs

    def draw(self: Self) -> None:
        self.sprite_list.draw()
