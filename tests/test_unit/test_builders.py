from typing import Final

import pytest
from inline_snapshot import snapshot

from imgproxykit import Transform
from imgproxykit.builders import PathBuilder
from imgproxykit.options import Quality, Resize
from imgproxykit.types import EMPTY

_SOURCE: Final = 'https://example.com/photo.jpg'
_WIDTH: Final = 300
_HEIGHT: Final = 200
_QUALITY: Final = 85


@pytest.mark.parametrize(
    ('source', 'expected'),
    [
        (_SOURCE, '/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'),
        (
            's3://bucket/café.jpg?version=1',
            '/czM6Ly9idWNrZXQvY2Fmw6kuanBnP3ZlcnNpb249MQ',
        ),
    ],
)
def test_source_path(*, source: str, expected: str) -> None:
    """Ensure that sources are encoded unchanged without Base64 padding."""
    assert PathBuilder()(source) == expected


def test_transform_path() -> None:
    """Ensure that transform options retain their order before the source."""
    transform = Transform(
        options=(
            Quality(_QUALITY),
            Resize(width=_WIDTH, height=_HEIGHT, mode='fill'),
        ),
        format='webp',
    )

    assert PathBuilder()(_SOURCE, transform=transform) == snapshot(
        '/q:85/rs:fill:300:200/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc.webp',
    )


def test_empty_transform_path() -> None:
    """Ensure that an empty transform adds neither options nor extension."""
    assert PathBuilder()(_SOURCE, transform=Transform()) == snapshot(
        '/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )


def test_format_only_transform_path() -> None:
    """Ensure that a transform can select a format without any options."""
    assert PathBuilder()(
        _SOURCE,
        transform=Transform(format='webp'),
    ) == snapshot('/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc.webp')


def test_presets_path() -> None:
    """Ensure that presets retain their order and accept an output format."""
    assert PathBuilder()(
        _SOURCE,
        presets=('thumbnail', 'watermarked'),
    ) == snapshot(
        '/pr:thumbnail:watermarked/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc',
    )
    assert PathBuilder()(
        _SOURCE,
        presets=('thumbnail',),
        output_format='avif',
    ) == snapshot('/pr:thumbnail/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc.avif')


@pytest.mark.parametrize('presets', [(), ('thumbnail',)])
def test_transform_with_presets(*, presets: tuple[str, ...]) -> None:
    """Ensure that even empty transforms and presets are mutually exclusive."""
    with pytest.raises(ValueError, match='Choose transform or presets'):
        PathBuilder()(_SOURCE, transform=Transform(), presets=presets)


@pytest.mark.parametrize('transform', [EMPTY, Transform()])
def test_output_format_without_presets(*, transform: Transform | EMPTY) -> None:
    """Ensure that a separate output format requires server presets."""
    with pytest.raises(ValueError, match='Set format on the Python transform'):
        PathBuilder()(_SOURCE, transform=transform, output_format='webp')
