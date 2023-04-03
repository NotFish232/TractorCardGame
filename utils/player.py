from typing import Callable

from typing_extensions import Self

from .card import Card
from .team import Team


class Player:
    next_avaliable_id: int = 1

    def __init__(
        self: Self, *, team: Team, cards: list[Card] = None, is_banker: bool = False
    ) -> None:
        self.team: Team = team
        self.cards: list[Card] = cards if cards is not None else []
        self.is_banker: bool = is_banker
        self.id: int = Player.next_avaliable_id
        Player.next_avaliable_id += 1

    @property
    def test(self: Self) -> None:
        pass

    def __eq__(self: Self, other: object) -> None:
        if isinstance(other, Player):
            return self.id == other.id

        raise NotImplementedError(
            "Comparision only supported with other player objects"
        )

    def __str__(self: Self) -> None:
        str_dict: str = ", ".join(
            f"{k}={v}" if k != "cards" else f"cards={len(v)}"
            for k, v in self.__dict__.items()
        )
        return f"Player({str_dict})"

    __repr__: Callable[..., str] = __str__
