from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Flip(Option):
    """
    Flip the image horizontally and/or vertically.

    Omitted axes remain :data:`~imgproxykit.types.EMPTY` and use
    imgproxy defaults.

    Attributes:
        horizontal: Whether to mirror the image horizontally.
        vertical: Whether to mirror the image vertically.

    Usage:

    .. code:: python

        Flip(horizontal=True)
        Flip(horizontal=True, vertical=True)

    See `imgproxy flip
    <https://docs.imgproxy.net/usage/processing#flip>`_.

    """

    horizontal: bool | EMPTY = EMPTY
    vertical: bool | EMPTY = EMPTY

    _name: ClassVar[OptionType] = 'fl'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.horizontal, self.vertical)
