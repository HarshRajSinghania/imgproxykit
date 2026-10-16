from typing import Literal

from imgproxykit.internal.empty import EMPTY as EMPTY  # noqa: PLC0414

type Argument = str | int | float | bool | EMPTY
type ResizeType = Literal[
    'fit',
    'fill',
    'fill-down',
    'force',
    'auto',
]
type Position = Literal[
    'no',
    'so',
    'ea',
    'we',
    'noea',
    'nowe',
    'soea',
    'sowe',
    'ce',
    'sm',
    'fp',
]
