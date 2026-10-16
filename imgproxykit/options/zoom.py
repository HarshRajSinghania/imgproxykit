from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Zoom(Option):
    """Multiply dimensions by one factor or separate X and Y factors."""

    factor_x: float
    factor_y: float | EMPTY = EMPTY

    _name: ClassVar[OptionType] = 'z'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.factor_x, self.factor_y)
