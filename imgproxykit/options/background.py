from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Background(Option):
    """Fill the background with a hex color or RGB tuple; omit to disable."""

    color: str | tuple[int, int, int] | EMPTY = EMPTY

    _name: ClassVar[OptionType] = 'bg'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return self.color if isinstance(self.color, tuple) else (self.color,)
