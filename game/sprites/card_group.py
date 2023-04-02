from functools import total_ordering
from pathlib import Path
import arcade
from typing_extensions import Self
from game.utils.card import Card

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
        is_visible: bool = True,
        is_interactable: bool = True,
    ) -> None:

        self.sprite_list: arcade.SpriteList = arcade.SpriteList()
        self.x_position: float = x_position
        self.y_position: float = y_position
        self.is_visible: bool = is_visible
        self.is_interactable: bool = is_interactable
        self.selected_cards = []

        for card in cards:
            filename: str = self.card_to_filename(card)
            sprite: arcade.Sprite = arcade.Sprite(ASSETS_FOLDER / filename, CARD_SCALE)
            self.sprite_list.append(sprite)

        if x_position is not None and y_position is not None:
            self.set_position(x_position, y_position)

    def set_position(self: Self, x_position: float, y_position: float) -> None:
        x_offset: float = x_position - CARD_SPACING * ((len(self.sprite_list) - 1) / 2)

        for i, sprite in enumerate(self.sprite_list):
            sprite.set_position(x_offset + i * CARD_SPACING, y_position)

    def card_to_filename(self: Self, card: Card) -> None:
        return str(card).replace(" ", "_").lower() + ".png"

    def toggle_state(self: Self, sprite: arcade.Sprite, state: bool) -> None:
        sprite.set_position(
            sprite.center_x, sprite.center_y + (1 if state else -1) * SELECT_CARD_DIST
        )

    def mouse_click(self: Self, x: int, y: int) -> None:
        if not self.is_visible or not self.is_interactable:
            return

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

    def get_selected_card_indices(
        self: Self, clear_selected: bool = True, clear_sprites: bool = True
    ) -> list[int]:
        indices: list[int] = self.selected_cards

        if clear_sprites:
            reversed_indices: list[int] = sorted(indices, reverse=True)
            for idx in reversed_indices:
                self.sprite_list.pop(idx)

            self.set_position()

        if clear_selected:
            self.selected_cards.clear()

        return indices

    def draw(self: Self) -> None:
        if self.is_visible:
            self.sprite_list.draw()
