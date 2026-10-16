from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.options.base import Option
from imgproxykit.types import EMPTY, Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Padding(Option):
    """
    Add padding using CSS side order; specify at least one side.

    Uses CSS side order and is applied after image transformations,
    except watermarking. Padding follows DPR and uses the background color.
    Supply at least one side; omitted arguments remain
    :data:`~imgproxykit.types.EMPTY`.

    Attributes:
        top: Top padding in pixels; fallback for omitted sides.
        right: Right padding; also used for an omitted left side.
        bottom: Bottom padding in pixels.
        left: Left padding in pixels.

    Usage:

    .. code:: python

        Padding(top=10)
        Padding(top=10, right=20, bottom=30, left=40)

    See `imgproxy padding
    <https://docs.imgproxy.net/usage/processing#padding>`_.

    """

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
