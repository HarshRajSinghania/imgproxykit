from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Trim(Option):
    """Trim the surrounding background with optional color and symmetry."""

    threshold: float
    color: str | EMPTY = EMPTY
    equal_hor: bool | EMPTY = EMPTY
    equal_ver: bool | EMPTY = EMPTY

    _name: ClassVar[OptionType] = 't'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.threshold, self.color, self.equal_hor, self.equal_ver)
