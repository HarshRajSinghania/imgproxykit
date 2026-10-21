from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import ClassVar

from imgproxykit.options.base import ScalarOption
from imgproxykit.types import OptionType


@dataclass(frozen=True, slots=True)
class Expires(ScalarOption[int]):
    """
    Reject the URL after the given Unix timestamp.

    imgproxy returns HTTP 404 after the supplied timestamp has expired.

    Accepts an integer Unix timestamp, a timezone-aware ``datetime``,
    or a ``timedelta`` relative to the current time. The value is
    normalized to a Unix timestamp in seconds at construction time so
    that a ``Transform`` containing this option remains reusable.

    Naive ``datetime`` values are rejected.

    Attributes:
        value: Expiration time as a Unix timestamp in seconds.

    Usage:

    >>> from datetime import datetime, timedelta, timezone
    >>> option = Expires(300)
    >>> option.arguments
    (300,)
    >>> option = Expires(timedelta(hours=1))
    >>> isinstance(option.value, int)
    True
    >>> option = Expires(datetime(2026, 1, 1, tzinfo=timezone.utc))
    >>> option.value == int(datetime(2026, 1, 1, tzinfo=timezone.utc).timestamp())
    True

    See `imgproxy expires
    <https://docs.imgproxy.net/usage/processing#expires>`_.

    """

    name: ClassVar[OptionType] = 'expires'

    def __init__(self, value: int | datetime | timedelta) -> None:
        normalized = self._normalize(value)
        # Bypass frozen dataclass init and set the field directly.
        object.__setattr__(self, 'value', normalized)
        self.__post_init__()

    @staticmethod
    def _normalize(value: int | datetime | timedelta) -> int:
        if isinstance(value, timedelta):
            # Resolve relative to now at construction for Transform reusability.
            value = int(
                (datetime.now(tz=timezone.utc) + value).timestamp()
            )
        elif isinstance(value, datetime):
            if value.tzinfo is None:
                msg = (
                    'Naive datetime is not allowed for Expires; '
                    'use a timezone-aware datetime'
                )
                raise ValueError(msg)
            value = int(value.timestamp())
        elif not isinstance(value, int):
            msg = (
                f'Expires expects int, datetime, or timedelta, '
                f'got {type(value).__name__}'
            )
            raise TypeError(msg)
        return value
