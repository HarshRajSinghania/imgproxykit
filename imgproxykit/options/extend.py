from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType, Position


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Extend(Option):
    """Extend the canvas to the target size using an optional gravity."""

    value: bool
    gravity: Position | EMPTY = EMPTY
    offset_x: float | EMPTY = EMPTY
    offset_y: float | EMPTY = EMPTY

    _name: ClassVar[OptionType] = 'ex'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (
            self.value,
            self.gravity,
            self.offset_x,
            self.offset_y,
        )
