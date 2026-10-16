from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Size(Option):
    """Set target dimensions, upscaling, and canvas extension."""

    width: int | EMPTY = EMPTY
    height: int | EMPTY = EMPTY
    enlarge: bool | EMPTY = EMPTY
    extend: bool | EMPTY = EMPTY

    _name: ClassVar[OptionType] = 's'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.width, self.height, self.enlarge, self.extend)
