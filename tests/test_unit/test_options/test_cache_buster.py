import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import CacheBuster


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (CacheBuster(value=''), 'cb:'),
        (CacheBuster(value='v1'), 'cb:v1'),
        (CacheBuster(value='café /:%?#'), 'cb:caf%C3%A9%20%2F%3A%25%3F%23'),
    ],
)
def test_cache_buster(*, option: CacheBuster, expected: str) -> None:
    """Ensure that cache busters escape reserved characters and Unicode."""
    assert serialize_option(option) == expected
