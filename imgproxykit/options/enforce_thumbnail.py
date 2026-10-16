from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class EnforceThumbnail(Option):
    """Use an embedded HEIC or AVIF thumbnail when available."""

    value: bool

    _name: ClassVar[OptionType] = 'eth'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
