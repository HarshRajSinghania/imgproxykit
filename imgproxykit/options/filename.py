from dataclasses import dataclass
from typing import ClassVar, final, override

from imgproxykit.internal.encoding import encode_base64
from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Filename(Option):
    """Set the response filename using URL-safe Base64 encoding."""

    value: str

    _name: ClassVar[OptionType] = 'fn'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (encode_base64(self.value), True)
