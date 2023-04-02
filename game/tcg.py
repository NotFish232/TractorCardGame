import time

import arcade
from typing_extensions import Self

from game.utils.card import Card
from game.utils.card_deck import CardDeck
from game.utils.infoset import InfoSet
from game.utils.player import Player
from game.utils.team import Team

from .sprites.board import Board
from .sprites.card import CardSprite

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
        self.banker_card_sprites: arcade.SpriteList = arcade.SpriteList()
        self.card_sprites: list[arcade.SpriteList] = [
            arcade.SpriteList() for _ in range(number_of_players)
        ]
        self.card_deck: CardDeck = CardDeck()
        self.infoset.teams = [Team(), Team()]
        self.infoset.players = [
            Player(team=self.infoset.teams[i % 2 != 0])
            for i in range(number_of_players)
        ]

        self.set_update_rate(1 / FPS)
        self.deal_cards()
        self.set_card_positions()

        print(self.infoset)

    def deal_cards(self: Self) -> None:
        for _ in range(NUM_DEAL_CARDS):
            for i, player in enumerate(self.infoset.players):
                card: Card = self.card_deck.deal_card()
                player.cards.append(card)
                self.card_sprites[i].append(CardSprite(card))

        while self.card_deck.has_cards():
            card: Card = self.card_deck.deal_card()
            self.infoset.bank_cards.append(card)
            self.banker_card_sprites.append(CardSprite(card))

    def set_card_positions(self: Self) -> None:
        interval: int = 40
        x_offset: float = SCREEN_WIDTH / 2 - interval * 12.5
        y_offset: float = SCREEN_HEIGHT * 5 / 32

        for card_set in self.card_sprites:
            for i, card_sprite in enumerate(card_set):
                card_sprite.set_position(x_offset + i * interval, y_offset)

    def next_turn(self: Self) -> None:
        self.board.rotate()

        while not self.board.is_rotating:
            time.sleep(1 / FPS)

    def draw_cards(self: Self) -> None:
        card_set: arcade.SpriteList = self.card_sprites[self.current_player_index]
        for card_sprite in card_set:
            card_sprite.draw()

    def on_update(self: Self, delta: float) -> None:
        pass

    def on_draw(self: Self) -> None:
        self.clear(BACKGROUND_COLOR)
        self.board.draw()
        self.draw_cards()
