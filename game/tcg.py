import time

import arcade
from typing_extensions import Self

from game.utils.card import Card
from game.utils.card_deck import CardDeck
from game.utils.infoset import InfoSet
from game.utils.player import Player
from game.utils.team import Team

from .sprites.board import Board
from .sprites.card_group import CardGroup

BACKGROUND_COLOR: arcade.Color = (211, 211, 211)
SCREEN_WIDTH: int = 1200
SCREEN_HEIGHT: int = 800
SCREEN_TITLE: str = "Tractor Card Game"

FPS: int = 60

NUM_DEAL_CARDS: int = 26


class TractorCardGame(arcade.Window):
    def __init__(self: Self, *, number_of_players: int = 6) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.board: Board = Board(SCREEN_WIDTH, SCREEN_HEIGHT, number_of_players)
        self.number_of_players: int = number_of_players
        self.current_player_index: int = 0

        self.infoset: InfoSet = InfoSet()
        self.banker_card_sprites: CardGroup = None
        self.card_sprites: list[CardGroup] = []
        self.card_deck: CardDeck = CardDeck()
        self.infoset.teams = [Team(), Team()]
        self.infoset.players = [
            Player(team=self.infoset.teams[i % 2 != 0])
            for i in range(number_of_players)
        ]

        self.set_update_rate(1 / FPS)
        self.deal_cards()

    def deal_cards(self: Self) -> None:
        x_position: float = SCREEN_WIDTH / 2
        y_position: float = SCREEN_HEIGHT * 1 / 8

        for _ in range(NUM_DEAL_CARDS):
            for player in self.infoset.players:
                card: Card = self.card_deck.deal_card()
                player.cards.append(card)

        self.card_sprites = [
            CardGroup(
                p.cards,
                x_position,
                y_position,
                is_visible=(i == self.current_player_index),
            )
            for i, p in enumerate(self.infoset.players)
        ]

        while self.card_deck.has_cards():
            card: Card = self.card_deck.deal_card()
            self.infoset.bank_cards.append(card)

        self.banker_card_sprites = CardGroup(self.infoset.bank_cards, is_visible=False)

    def next_round(self: Self) -> None:
        pass

    def reset_game(self: Self) -> None:
        pass

    def next_turn(self: Self) -> None:
        def next_turn_callback() -> None:
            self.current_player_index += 1

            if self.current_player_index >= len(self.infoset.players):
                self.next_round()

        self.board.rotate(next_turn_callback)

    def on_mouse_press(self: Self, x: int, y: int, button: int, modifiers: int) -> None:
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        for card_group in self.card_sprites:
            card_group.mouse_click(x, y)

        self.banker_card_sprites.mouse_click(x, y)

    def on_update(self: Self, delta: float) -> None:
        pass

    def on_draw(self: Self) -> None:
        self.clear(BACKGROUND_COLOR)
        self.board.draw()
        self.card_sprites[self.current_player_index].draw()

        x_position: float = SCREEN_WIDTH / 2
        y_position: float = SCREEN_HEIGHT * 9 / 32
        arcade.draw_text(
            str(self.infoset.players[self.current_player_index]),
            x_position,
            y_position,
            color=arcade.color.BLACK,
            anchor_x="center",
            anchor_y="center",
        )
