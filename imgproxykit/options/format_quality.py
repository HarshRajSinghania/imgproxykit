from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, FormatType, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class FormatQuality(Option):
    """
    Set quality for each supplied output format.

    Adds or overrides server quality settings for the listed formats.

    Attributes:
        qualities: Ordered pairs of output format and quality percentage.

    Usage:

    .. code:: python

        FormatQuality(qualities=(('jpg', 85), ('webp', 80)))

    See `imgproxy format quality
    <https://docs.imgproxy.net/usage/processing#format-quality>`_.

    """

    qualities: tuple[tuple[FormatType, int], ...]

    _name: ClassVar[OptionType] = 'fq'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return tuple(argument for pair in self.qualities for argument in pair)
