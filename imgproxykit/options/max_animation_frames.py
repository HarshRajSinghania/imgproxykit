from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class MaxAnimationFrames(Option):
    """Override animation frame limit; requires ALLOW_SECURITY_OPTIONS."""

    value: int

    _name: ClassVar[OptionType] = 'maf'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
