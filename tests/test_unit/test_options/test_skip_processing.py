import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import SkipProcessing


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (SkipProcessing(formats=()), 'skp'),
        (SkipProcessing(formats=('svg',)), 'skp:svg'),
        (SkipProcessing(formats=('svg', 'gif')), 'skp:svg:gif'),
    ],
)
def test_skip_processing(*, option: SkipProcessing, expected: str) -> None:
    """Ensure that skipped formats retain their order and allow omission."""
    assert serialize_option(option) == expected
