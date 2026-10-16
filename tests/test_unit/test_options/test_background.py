import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Background


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Background(), 'bg'),
        (Background(color='ff0080'), 'bg:ff0080'),
        (Background(color=(0, 128, 255)), 'bg:0:128:255'),
    ],
)
def test_background(*, option: Background, expected: str) -> None:
    """Ensure that backgrounds accept hex colors, RGB tuples, and omission."""
    assert serialize_option(option) == expected
