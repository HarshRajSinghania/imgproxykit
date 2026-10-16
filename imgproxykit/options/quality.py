from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True)
class Quality(Option):
    """
    Set output image quality.

    Attributes:
        value: Quality percentage. Zero delegates to server quality settings.

    Usage:

    .. code:: python

        Quality(85)

    See `imgproxy quality
    <https://docs.imgproxy.net/usage/processing#quality>`_.

    """

    # Public API:
    value: int

    # Private API:
    _name: ClassVar[OptionType] = 'q'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (self.value,)
