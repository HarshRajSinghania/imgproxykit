from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Flip(Option):
    """Flip the image horizontally and/or vertically."""

    horizontal: bool | EMPTY = EMPTY
    vertical: bool | EMPTY = EMPTY

    _name: ClassVar[OptionType] = 'fl'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.horizontal, self.vertical)
