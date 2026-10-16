from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Padding(Option):
    """Add padding using CSS side order; specify at least one side."""

    top: int | EMPTY = EMPTY
    right: int | EMPTY = EMPTY
    bottom: int | EMPTY = EMPTY
    left: int | EMPTY = EMPTY

    _name: ClassVar[OptionType] = 'pd'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.top, self.right, self.bottom, self.left)
