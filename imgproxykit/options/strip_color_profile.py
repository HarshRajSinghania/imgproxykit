from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class StripColorProfile(Option):
    """Convert the embedded profile to sRGB and remove it."""

    value: bool

    _name: ClassVar[OptionType] = 'scp'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
