from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, FormatType, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class FormatQuality(Option):
    """Set quality for each supplied output format."""

    qualities: tuple[tuple[FormatType, int], ...]

    _name: ClassVar[OptionType] = 'fq'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return tuple(argument for pair in self.qualities for argument in pair)
