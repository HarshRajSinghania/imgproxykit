from datetime import datetime, timedelta, timezone

import pytest

from imgproxykit.options import Expires
from imgproxykit.serialization import PathSerializer


def test_expires_int() -> None:
    """Ensure integer timestamps are accepted and serialized unchanged."""
    option = Expires(1_700_000_000)

    assert option.value == 1_700_000_000
    assert option.arguments == (1_700_000_000,)
    assert (
        PathSerializer()._serialize_segment(option.name, option.arguments)
        == 'expires:1700000000'
    )


def test_expires_timedelta() -> None:
    """Ensure timedelta is resolved to a timestamp at construction time."""
    before = int(datetime.now(tz=timezone.utc).timestamp())
    option = Expires(timedelta(hours=1))
    after = int(datetime.now(tz=timezone.utc).timestamp())

    # Allow a small window for clock movement.
    assert before + 3600 <= option.value <= after + 3600 + 1
    assert isinstance(option.value, int)
    assert option.arguments == (option.value,)


def test_expires_aware_datetime() -> None:
    """Ensure timezone-aware datetimes are converted to Unix timestamps."""
    dt = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
    option = Expires(dt)

    expected = int(dt.timestamp())
    assert option.value == expected
    assert option.arguments == (expected,)
    assert (
        PathSerializer()._serialize_segment(option.name, option.arguments)
        == f'expires:{expected}'
    )


def test_expires_naive_datetime_rejected() -> None:
    """Ensure naive datetimes raise ValueError."""
    with pytest.raises(ValueError, match='Naive datetime is not allowed'):
        Expires(datetime(2026, 1, 1))


def test_expires_invalid_type() -> None:
    """Ensure unsupported types raise TypeError."""
    with pytest.raises(TypeError, match='Expires expects int, datetime, or timedelta'):
        Expires('not-a-time')  # type: ignore[arg-type]
