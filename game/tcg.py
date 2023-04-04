from typing import Callable

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
    def __init__(
        self: Self,
        *,
        number_of_players: int = 6,
        predictors: list[Callable[[InfoSet], list[Card]]] = None
    ) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.number_of_players: int = number_of_players

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
        self.info_popup: gui.UITextArea = None
        self.ui_manager.enable()

        assert (
            predictors is None or len(predictors) == number_of_players
        ), "number of predictors must be the same as the number of players"

        # list of callables that should take an infoset and return a move
        self.predictors: list[Callable[[InfoSet], list[Card]]] = (
            predictors or [None] * number_of_players
        )

        self.deal_cards()
        self.set_card_positions()
        self.on_turn_start()

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

        info_btn: gui.UIFlatButton = gui.UIFlatButton(
            text="Info",
            width=WIDTH,
            style={
                "bg_color": arcade.color.BLUE_BELL,
                "border_color": arcade.color.WHITE,
            },
        )
        info_btn.on_click = self.on_info_btn_click

        v_box.add(select_cards_btn.with_space_around(bottom=PADDING))
        v_box.add(info_btn.with_space_around(bottom=PADDING))

        ui_mgr.add(v_box)

        return ui_mgr

    def on_info_btn_click(self: Self, e: gui.UIOnClickEvent) -> None:
        self.info_popup: gui.UITextArea = gui.UITextArea(
            x=SCREEN_WIDTH * 1 / 8,
            y=SCREEN_HEIGHT * 1 / 8,
            width=SCREEN_WIDTH * 3 / 4,
            height=SCREEN_HEIGHT * 3 / 4,
            text=str(self.infoset),
            text_color=arcade.color.BLACK,
        )

        self.ui_manager.add(self.info_popup)

        self.ui_manager.disable()

    def on_select_cards_btn_click(self: Self, e: gui.UIOnClickEvent) -> None:
        current_player: Player = self.infoset.players[self.infoset.cur_player_idx]
        selected_card_idxs: list[int] = self.card_sprites[
            self.infoset.cur_player_idx
        ].get_selected_card_idxs()
        selected_cards: list[Card] = []

        for idx in selected_card_idxs:
            selected_cards.append(current_player.cards.pop(idx))

        self.infoset.round_play_seq.append(selected_cards)
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
                is_visible=(i == self.infoset.cur_player_idx),
            )
            for i, player in enumerate(self.infoset.players)
        ]

        self.banker_card_sprites = CardGroup(self.infoset.bank_cards, is_visible=False)


    def next_round(self: Self) -> None:
        self.infoset.cur_player_idx = 0
        self.infoset.game_play_seq.extend(self.infoset.round_play_seq)
        self.infoset.round_play_seq.clear()

    def on_turn_start(self: Self) -> None:
        self.card_sprites[self.infoset.cur_player_idx].is_visible = True

        predictor: Callable[[InfoSet], list[Card]] = self.predictors[
            self.infoset.cur_player_idx
        ]

        if predictor is not None:

            def _make_prediction(_: float) -> None:
                arcade.unschedule(_make_prediction)
                move: list[Card] = predictor(self.infoset)
                self.infoset.round_play_seq.append(move)
                self.board.add_cards(move)
                self.next_turn()

            arcade.schedule(_make_prediction, 1)

    def next_turn(self: Self) -> None:
        def next_turn_callback() -> None:
            self.card_sprites[self.infoset.cur_player_idx].is_visible = False
            self.infoset.cur_player_idx += 1

            if self.infoset.cur_player_idx >= len(self.infoset.players):
                self.next_round()

            self.on_turn_start()

        if self.infoset.cur_player_idx == len(self.infoset.players) - 1:

            def _end_round(_: float) -> None:
                arcade.unschedule(_end_round)
                self.board.clear_cards()
                self.board.rotate(next_turn_callback)

            arcade.schedule(_end_round, 2)
        else:
            self.board.rotate(next_turn_callback)

    def on_mouse_press(self: Self, x: int, y: int, button: int, modifiers: int) -> None:
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        if self.info_popup is not None:
            self.info_popup.parent.remove(self.info_popup)
            self.info_popup = None
            self.ui_manager.enable()
            return

        for card_group in self.card_sprites:
            card_group.mouse_click(x, y)

        self.banker_card_sprites.mouse_click(x, y)

    def on_draw(self: Self) -> None:
        self.clear(BACKGROUND_COLOR)
        self.board.draw()
        self.card_sprites[self.infoset.cur_player_idx].draw()

        # write play information
        arcade.draw_text(
            str(self.infoset.players[self.infoset.cur_player_idx]),
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT * 9 / 32,
            color=arcade.color.BLACK,
            anchor_x="center",
            anchor_y="center",
        )

        # draw backdrop of info if popup is up
        if self.info_popup is not None:
            arcade.draw_rectangle_filled(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                SCREEN_WIDTH * 13 / 16,
                SCREEN_HEIGHT * 13 / 16,
                arcade.color.LIGHT_GRAY,
            )
            arcade.draw_rectangle_outline(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                SCREEN_WIDTH * 13 / 16,
                SCREEN_HEIGHT * 13 / 16,
                arcade.color.BLACK,
                3,
            )

        # renders UI
        self.ui_manager.draw()
