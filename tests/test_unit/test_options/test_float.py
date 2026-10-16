from typing import Final

import pytest

from imgproxykit import options
from imgproxykit.internal.serialization import serialize_option

_ZERO: Final = 0.0  # noqa: WPS358
_FACTOR: Final = 1.5


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (options.DPR(value=_ZERO), 'dpr:0.0'),
        (options.DPR(value=_FACTOR), 'dpr:1.5'),
        (options.Blur(value=_ZERO), 'bl:0.0'),
        (options.Blur(value=_FACTOR), 'bl:1.5'),
        (options.Sharpen(value=_ZERO), 'sh:0.0'),
        (options.Sharpen(value=_FACTOR), 'sh:1.5'),
        (options.MaxSrcResolution(value=_ZERO), 'msr:0.0'),
        (options.MaxSrcResolution(value=_FACTOR), 'msr:1.5'),
        (options.MaxAnimationFrameResolution(value=_ZERO), 'mafr:0.0'),
        (options.MaxAnimationFrameResolution(value=_FACTOR), 'mafr:1.5'),
    ],
)
def test_float_options(*, option: options.Option, expected: str) -> None:
    """Ensure that float options preserve zeroes and fractional values."""
    assert serialize_option(option) == expected
