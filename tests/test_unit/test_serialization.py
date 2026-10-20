from typing import Final

import pytest

from imgproxykit import Transform
from imgproxykit.options import Format, Preset, Quality, Resize
from imgproxykit.serialization import PathSerializer
from imgproxykit.types import Argument

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
    assert PathSerializer()(source) == expected


def test_transform_path() -> None:
    """Ensure that transform options retain their order before the source."""
    transform = Transform(
        Quality(_QUALITY),
        Resize(width=_WIDTH, height=_HEIGHT, mode='fill'),
        Format('webp'),
    )

    assert PathSerializer()(_SOURCE, transform=transform) == (
        '/quality:85/resize:fill:300:200/format:webp/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )


def test_empty_transform_path() -> None:
    """Ensure that an empty transform adds no processing segments."""
    assert PathSerializer()(_SOURCE, transform=Transform()) == (
        '/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )


def test_empty_presets_path() -> None:
    """Ensure that explicit empty presets retain the preset segment."""
    assert (
        PathSerializer()(_SOURCE, transform=Transform(Preset(names=())))
        == '/preset/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )


def test_presets_path() -> None:
    """Ensure that preset names retain their order within a segment."""
    transform = Transform(Preset(names=('thumbnail', 'watermarked')))

    assert PathSerializer()(_SOURCE, transform=transform) == (
        '/preset:thumbnail:watermarked/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )


def test_interleaved_presets() -> None:
    """Ensure that preset references preserve positions around overrides."""
    transform = Transform(
        Preset(names=('thumbnail',)),
        Quality(_QUALITY),
        Preset(names=('watermarked',)),
    )
    assert PathSerializer()(_SOURCE, transform=transform) == (
        '/preset:thumbnail/quality:85/preset:watermarked/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )


def test_interleaved_formats() -> None:
    """Ensure that format options preserve their order around presets."""
    transform = Transform(
        Format('webp'),
        Preset(names=('thumbnail',)),
        Format('avif'),
    )
    assert PathSerializer()(_SOURCE, transform=transform) == (
        '/format:webp/preset:thumbnail/format:avif/'
        'aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
    )


@pytest.mark.parametrize(
    ('arguments', 'expected'),
    [
        ((), 'resize'),
        ((None, None), 'resize'),
        (('fill', None, None), 'resize:fill'),
        ((None, _WIDTH, None), 'resize::300'),
        ((_WIDTH, None, _HEIGHT), 'resize:300::200'),
        (('fill', None, None, True), 'resize:fill:::1'),
        ((True, False), 'resize:1:0'),
        ((0.0, 1.5), 'resize:0.0:1.5'),  # noqa: WPS358
        (('', None), 'resize:'),
        ((False, None), 'resize:0'),
        ((0, None), 'resize:0'),
        (('café',), 'resize:café'),
    ],
)
def test_serialize_segment(
    *,
    arguments: tuple[Argument, ...],
    expected: str,
) -> None:
    """Ensure that arguments retain their positions and explicit values."""
    assert PathSerializer._serialize_segment('resize', arguments) == expected
