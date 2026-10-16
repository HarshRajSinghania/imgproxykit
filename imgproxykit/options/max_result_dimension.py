from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class MaxResultDimension(Option):
    """Override output dimension limit; requires ALLOW_SECURITY_OPTIONS."""

    value: int

    _name: ClassVar[OptionType] = 'mrd'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
