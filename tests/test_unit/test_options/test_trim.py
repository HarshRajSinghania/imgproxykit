import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Trim


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Trim(threshold=0), 't:0'),
        (
            Trim(
                threshold=10,
                color='ffffff',
                equal_hor=True,
                equal_ver=False,
            ),
            't:10:ffffff:1:0',
        ),
        (Trim(threshold=10, equal_ver=False), 't:10:::0'),
    ],
)
def test_trim(*, option: Trim, expected: str) -> None:
    """Ensure that trim retains its threshold, color, and symmetry flags."""
    assert serialize_option(option) == expected
