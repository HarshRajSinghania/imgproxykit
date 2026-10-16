import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import ResizingType


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (ResizingType(value='fit'), 'rt:fit'),
        (ResizingType(value='fill'), 'rt:fill'),
        (ResizingType(value='auto'), 'rt:auto'),
    ],
)
def test_resizing_type(*, option: ResizingType, expected: str) -> None:
    """Ensure that resizing strategies use the resizing type segment."""
    assert serialize_option(option) == expected
