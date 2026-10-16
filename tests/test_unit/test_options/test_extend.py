from typing import Final

import pytest

from imgproxykit.internal.serialization import serialize_option
from imgproxykit.options import Extend

_OFFSET_X: Final = 0.25
_OFFSET_Y: Final = 0.75


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (Extend(value=False), 'ex:0'),
        (
            Extend(
                value=True,
                gravity='fp',
                offset_x=_OFFSET_X,
                offset_y=_OFFSET_Y,
            ),
            'ex:1:fp:0.25:0.75',
        ),
        (Extend(value=True, offset_y=0), 'ex:1:::0'),
    ],
)
def test_extend(*, option: Extend, expected: str) -> None:
    """Ensure that extension retains its flag, anchor, and offset positions."""
    assert serialize_option(option) == expected
