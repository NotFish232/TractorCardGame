import math
from typing import Callable

import arcade
from typing_extensions import Self

from utils.card import Card

from .card_group import CardGroup

BOARD_COLOR: arcade.Color = (53, 101, 77)
BORDER_COLOR: arcade.Color = (61, 16, 5)
BORDER_WIDTH: int = 5


class Board:
    def __init__(
        self: Self, screen_width: int, screen_height: int, number_of_sides: int
    ) -> None:
        self.screen_width: int = screen_width
        self.screen_height: int = screen_height
        self.number_of_sides: int = number_of_sides
        self.is_rotating: bool = False
        self.points: arcade.PointList = []

        self.card_sprites: list[CardGroup] = []

        self.build_board()

    def add_cards(self: Self, cards: list[Card]) -> None:
        card_group: CardGroup = CardGroup(cards, size=0.8)

        self.card_sprites = [card_group] + self.card_sprites

        self.build_board()

    def clear_cards(self: Self) -> None:
        self.card_sprites.clear()

    def rotate(self: Self, callback: Callable[..., None] = None, *args, **kwargs) -> None:
        self.is_rotating = True
        # number of frames to run animation
        NUMBER_OF_FRAMES: int = 100
        iteration: int = 0
        full_rotation_angle: float = 2 * math.pi / self.number_of_sides

        def _rotate(_: int) -> None:
            nonlocal iteration
            iteration += 1

            self.build_board(full_rotation_angle * (iteration / NUMBER_OF_FRAMES))

            if iteration == NUMBER_OF_FRAMES:
                arcade.unschedule(_rotate)
                self.is_rotating = False

                if callback is not None:
                    callback(*args, **kwargs)

        arcade.schedule(_rotate, 0.01)

    def build_board(self: Self, rotation: float = 0) -> None:
        self.points.clear()

        center_x: float = self.screen_width / 2
        center_y: float = self.screen_height * 5 / 8

        angle_interval: float = 2 * math.pi / self.number_of_sides
        side_length: float = self.screen_height / 3
        initial_angle: float = 4 * math.pi / self.number_of_sides

        for i in range(self.number_of_sides):
            angle: float = initial_angle + angle_interval * (i + 0.5) + rotation
            card_angle: float = math.pi - (
                initial_angle + angle_interval * i + rotation
            )

            x: float = center_x + math.sin(angle) * side_length
            y: float = center_y + math.cos(angle) * side_length

            if i != 0 and i <= len(self.card_sprites):
                card_group: CardGroup = self.card_sprites[i - 1]
                last_x, last_y = self.points[-1]

                card_x = (9 * (last_x + x) / 2 + center_x) / 10
                card_y = (9 * (last_y + y) / 2 + center_y) / 10

                card_group.set_position(card_x, card_y, card_angle)

            self.points.append((x, y))

    def draw(self: Self) -> None:
        arcade.draw_polygon_filled(self.points, BOARD_COLOR)
        arcade.draw_polygon_outline(self.points, BORDER_COLOR, BORDER_WIDTH)

        for card_group in self.card_sprites:
            card_group.draw()
