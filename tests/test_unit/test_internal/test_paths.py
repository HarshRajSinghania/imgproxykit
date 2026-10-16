from typing import Final

import pytest

from imgproxykit.internal.paths import build_path
from imgproxykit.types import EMPTY, FormatType

_SOURCE: Final = 'https://example.com/photo.jpg'


@pytest.mark.parametrize(
    ('options', 'output_format', 'expected'),
    [
        (
            (),
            EMPTY,
            '/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
        ),
        (
            (),
            'webp',
            '/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc.webp',
        ),
        (
            ('q:85', 'rs:fill:300:200'),
            EMPTY,
            '/q:85/rs:fill:300:200/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
        ),
        (
            ('q:85', 'rs:fill:300:200'),
            'avif',
            '/q:85/rs:fill:300:200/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc.avif',
        ),
    ],
)
def test_build_path(
    *,
    options: tuple[str, ...],
    output_format: FormatType | EMPTY,
    expected: str,
) -> None:
    """Ensure that paths retain option order and append the selected format."""
    assert (
        build_path(
            _SOURCE,
            options=options,
            output_format=output_format,
        )
        == expected
    )
