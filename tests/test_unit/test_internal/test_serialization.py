from typing import Final

import pytest

from imgproxykit.internal.serialization import (
    serialize_option,
    serialize_segment,
)
from imgproxykit.options import Resize
from imgproxykit.types import EMPTY, Argument

_WIDTH: Final = 300
_HEIGHT: Final = 200


@pytest.mark.parametrize(
    ('arguments', 'expected'),
    [
        ((), 'rs'),
        ((EMPTY,), 'rs'),
        ((EMPTY, EMPTY), 'rs'),
        (('fill', EMPTY, EMPTY), 'rs:fill'),
        ((EMPTY, _WIDTH, EMPTY), 'rs::300'),
        ((_WIDTH, EMPTY, _HEIGHT), 'rs:300::200'),
        (('fill', EMPTY, EMPTY, True), 'rs:fill:::1'),
        ((True, False), 'rs:1:0'),
        ((0,), 'rs:0'),
        ((0.0, 1.5), 'rs:0.0:1.5'),  # noqa: WPS358
        (('',), 'rs:'),
        (('', EMPTY), 'rs:'),
        ((False, EMPTY), 'rs:0'),
        ((0, EMPTY), 'rs:0'),
        (('café',), 'rs:café'),
    ],
)
def test_serialize_segment(
    *,
    arguments: tuple[Argument, ...],
    expected: str,
) -> None:
    """Ensure that arguments retain their positions and explicit values."""
    assert serialize_segment('rs', arguments) == expected


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (
            Resize(
                width=_WIDTH,
                height=_HEIGHT,
                mode='fill',
                enlarge=False,
                extend=True,
            ),
            'rs:fill:300:200:0:1',
        ),
        (
            Resize(height=_HEIGHT),
            'rs:::200',
        ),
    ],
)
def test_serialize_option(*, option: Resize, expected: str) -> None:
    """Ensure that an option uses its name and protocol argument order."""
    assert serialize_option(option) == expected
