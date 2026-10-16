from typing import Final

import pytest

from imgproxykit import options
from imgproxykit.internal.serialization import serialize_option

_VALUE: Final = 42


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (options.Width(value=0), 'w:0'),
        (options.Width(value=_VALUE), 'w:42'),
        (options.Height(value=0), 'h:0'),
        (options.Height(value=_VALUE), 'h:42'),
        (options.MinWidth(value=0), 'mw:0'),
        (options.MinWidth(value=_VALUE), 'mw:42'),
        (options.MinHeight(value=0), 'mh:0'),
        (options.MinHeight(value=_VALUE), 'mh:42'),
        (options.Quality(value=0), 'q:0'),
        (options.Quality(value=_VALUE), 'q:42'),
        (options.Pixelate(value=0), 'pix:0'),
        (options.Pixelate(value=_VALUE), 'pix:42'),
        (options.Rotate(value=0), 'rot:0'),
        (options.Rotate(value=_VALUE), 'rot:42'),
        (options.Expires(value=0), 'exp:0'),
        (options.Expires(value=_VALUE), 'exp:42'),
        (options.MaxBytes(value=0), 'mb:0'),
        (options.MaxBytes(value=_VALUE), 'mb:42'),
        (options.MaxResultDimension(value=0), 'mrd:0'),
        (options.MaxResultDimension(value=_VALUE), 'mrd:42'),
        (options.MaxSrcFileSize(value=0), 'msfs:0'),
        (options.MaxSrcFileSize(value=_VALUE), 'msfs:42'),
        (options.MaxAnimationFrames(value=0), 'maf:0'),
        (options.MaxAnimationFrames(value=_VALUE), 'maf:42'),
    ],
)
def test_integer_options(*, option: options.Option, expected: str) -> None:
    """Ensure that integer options preserve explicit zeroes and values."""
    assert serialize_option(option) == expected
