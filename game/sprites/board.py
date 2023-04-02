import math
from typing import Callable

import arcade
from typing_extensions import Self

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

        self.points: arcade.PointList = self.make_points()

    def rotate(self: Self, callback: Callable[..., None] = None) -> None:
        self.is_rotating = True
        # number of frames to run animation
        NUMBER_OF_FRAMES: int = 100
        iteration: int = 0
        full_rotation_angle: float = 2 * math.pi / self.number_of_sides

        def _rotate(_: int) -> None:
            nonlocal iteration
            iteration += 1

            self.points = self.make_points(
                full_rotation_angle * (iteration / NUMBER_OF_FRAMES)
            )

            if iteration == NUMBER_OF_FRAMES:
                arcade.unschedule(_rotate)
                self.is_rotating = False

                if callback is not None:
                    callback()

        arcade.schedule(_rotate, 0.01)

    def make_points(self: Self, rotation: float = 0) -> arcade.PointList:
        angle: float = 2 * math.pi / self.number_of_sides
        side_length: float = self.screen_height / 3
        points: arcade.PointList = []

        for i in range(self.number_of_sides):

            point: arcade.Point = (
                self.screen_width / 2
                + math.sin(angle * (i + 0.5) + rotation) * side_length,
                self.screen_height * 5 / 8
                + math.cos(angle * (i + 0.5) + rotation) * side_length,
            )

            points.append(point)

        return points

    def draw(self: Self) -> None:
        arcade.draw_polygon_filled(self.points, BOARD_COLOR)
        arcade.draw_polygon_outline(self.points, BORDER_COLOR, BORDER_WIDTH)
