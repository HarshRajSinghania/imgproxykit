from dataclasses import dataclass

from imgproxykit.types import EMPTY, Argument, Position, ResizeType


@dataclass(frozen=True, slots=True, init=False)
class Option:
    """An arbitrary imgproxy option."""

    name: str
    arguments: tuple[Argument, ...]

    def __init__(self, name: str, *arguments: Argument) -> None:
        """Store the option without interpreting server capabilities."""
        object.__setattr__(self, 'name', name)
        object.__setattr__(self, 'arguments', arguments)


@dataclass(frozen=True, slots=True, kw_only=True)
class Resize:
    """The imgproxy resize meta-option with explicit arguments only."""

    width: int | EMPTY = EMPTY
    height: int | EMPTY = EMPTY
    mode: ResizeType | EMPTY = EMPTY
    enlarge: bool | EMPTY = EMPTY
    extend: bool | EMPTY = EMPTY


@dataclass(frozen=True, slots=True)
class DPR:
    """The imgproxy device pixel ratio option."""

    value: float


@dataclass(frozen=True, slots=True, kw_only=True)
class Gravity:
    """The imgproxy gravity option with explicit arguments only."""

    position: Position
    offset_x: float | EMPTY = EMPTY
    offset_y: float | EMPTY = EMPTY
