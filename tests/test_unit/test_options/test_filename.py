import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Filename


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Filename(value=''), 'fn::1'),
        (Filename(value='product photo.jpg'), 'fn:cHJvZHVjdCBwaG90by5qcGc:1'),
        (Filename(value='café'), 'fn:Y2Fmw6k:1'),
    ],
)
def test_filename(*, option: Filename, expected: str) -> None:
    """Ensure that filenames use Base64 encoding with the encoding flag."""
    assert serialize_option(option) == expected
