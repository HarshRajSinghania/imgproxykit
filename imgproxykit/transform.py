from dataclasses import dataclass

from imgproxykit.options import Option
from imgproxykit.types import EMPTY, FormatType


@dataclass(frozen=True, slots=True, kw_only=True)
class Transform:
    """A reusable collection of processing options and output format."""

    options: tuple[Option, ...] = ()
    format: FormatType | EMPTY = EMPTY
