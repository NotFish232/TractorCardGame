import time
import math
import arcade
from arcade import gui
from typing_extensions import Self

from utils.card import Card
from utils.card_deck import CardDeck
from utils.infoset import InfoSet
from utils.player import Player
from utils.team import Team

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

        self.board: Board = Board(SCREEN_WIDTH, SCREEN_HEIGHT, number_of_players)
        self.ui_manager: gui.UIManager = self.make_ui()
        self.ui_manager.enable()

        self.deal_cards()
        self.set_card_positions()

        self.set_update_rate(1 / FPS)

    def make_ui(self: Self) -> gui.UIManager:
        PADDING: int = 15
        WIDTH: int = 150

        ui_mgr: gui.UIManager = gui.UIManager()
        v_box: gui.UIBoxLayout = gui.UIBoxLayout(
            x=SCREEN_WIDTH - WIDTH - PADDING, y=SCREEN_HEIGHT - PADDING
        )

        select_cards_btn: gui.UIFlatButton = gui.UIFlatButton(
            text="Select Cards",
            width=WIDTH,
            style={
                "bg_color": arcade.color.GREEN,
                "border_color": arcade.color.BLACK,
            },
        )
        select_cards_btn.on_click = self.on_select_cards_btn_click

        other_btn: gui.UIFlatButton = gui.UIFlatButton(text="other btn", width=WIDTH)

        v_box.add(select_cards_btn.with_space_around(bottom=PADDING))
        v_box.add(other_btn.with_space_around(bottom=PADDING))

        ui_mgr.add(v_box)

        return ui_mgr

    def on_select_cards_btn_click(self: Self, e: gui.UIOnClickEvent) -> None:
        current_player: Player = self.infoset.players[self.current_player_index]
        selected_card_idxs: list[int] = self.card_sprites[
            self.current_player_index
        ].get_selected_card_idxs()
        selected_cards: list[Card] = []

        for idx in selected_card_idxs:
            selected_cards.append(current_player.cards.pop(idx))

        self.board.add_cards(selected_cards)

        self.next_turn()

    def deal_cards(self: Self) -> None:
        for _ in range(NUM_DEAL_CARDS):
            for player in self.infoset.players:
                card: Card = self.card_deck.deal_card()
                player.cards.append(card)

        while self.card_deck.has_cards():
            card: Card = self.card_deck.deal_card()
            self.infoset.bank_cards.append(card)

    def set_card_positions(self: Self) -> None:
        x_position: float = SCREEN_WIDTH / 2
        y_position: float = SCREEN_HEIGHT * 1 / 8

        self.card_sprites = [
            CardGroup(
                player.cards,
                x_position,
                y_position,
                is_visible=(i == self.current_player_index),
            )
            for i, player in enumerate(self.infoset.players)
        ]

        self.banker_card_sprites = CardGroup(self.infoset.bank_cards, is_visible=False)

    def next_round(self: Self) -> None:
        pass

    def reset_game(self: Self) -> None:
        pass

    def next_turn(self: Self) -> None:
        def next_turn_callback() -> None:
            self.card_sprites[self.current_player_index].is_visible = False
            self.current_player_index += 1
            self.card_sprites[self.current_player_index].is_visible = True

            if self.current_player_index >= len(self.infoset.players) - 1:
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

        # write play information
        arcade.draw_text(
            str(self.infoset.players[self.current_player_index]),
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT * 9 / 32,
            color=arcade.color.BLACK,
            anchor_x="center",
            anchor_y="center",
        )

        # renders UI
        self.ui_manager.draw()
