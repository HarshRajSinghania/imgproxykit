from typing import Literal

from imgproxykit.internal.empty import EMPTY as EMPTY  # noqa: PLC0414

type Argument = str | int | float | bool | EMPTY
type OptionType = Literal[
    'rs',
    'g',
    'dpr',
    'q',
    'wm',
]
type WatermarkPosition = Literal[
    'ce',
    'no',
    'so',
    'ea',
    'we',
    'noea',
    'nowe',
    'soea',
    'sowe',
    're',
]
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
