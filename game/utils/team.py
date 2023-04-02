from typing import Callable

from typing_extensions import Self


class Team:
    next_avaliable_id: int = 1

    def __init__(self: Self) -> None:
        self.points: int = 0
        self.id: int = Team.next_avaliable_id
        Team.next_avaliable_id += 1

    def __eq__(self: Self, other: object) -> None:
        if isinstance(other, Team):
            return self.id == other.id

        raise NotImplementedError("Comparision only supported with other team objects")

    def __str__(self: Self) -> str:
        return f"Team{self.id} (pts={self.points})"

    __repr__: Callable[..., str] = __str__
