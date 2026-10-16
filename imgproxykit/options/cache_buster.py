from dataclasses import dataclass
from typing import ClassVar, final, override
from urllib.parse import quote

from imgproxykit.options.base import Option
from imgproxykit.types import Argument, OptionType


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class CacheBuster(Option):
    """Add an escaped version string to the signed URL to bypass caches."""

    value: str

    _name: ClassVar[OptionType] = 'cb'

    @property
    @override
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
        return (quote(self.value, safe=''),)
