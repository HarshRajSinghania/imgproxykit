import base64

from imgproxykit.options import DPR, Gravity, Option, Resize
from imgproxykit.types import EMPTY, Argument


def build_path(
    source: str,
    *,
    options: tuple[str, ...],
    output_format: str | EMPTY = EMPTY,
) -> str:
    """Build the path before signing it."""
    segments = '/'.join((*options, encode(source)))
    path = f'/{segments}'
    return path if output_format is EMPTY else f'{path}.{output_format}'


def encode(value: str | bytes) -> str:
    """Encode source text or a signature without Base64 padding."""
    raw = value.encode() if isinstance(value, str) else value
    return base64.urlsafe_b64encode(raw).rstrip(b'=').decode()


def serialize_option(value: Option | Resize | Gravity | DPR) -> str:
    """Serialize option data without exposing serialization in the API."""
    if isinstance(value, Resize):
        value = Option(
            'rs',
            value.mode,
            value.width,
            value.height,
            value.enlarge,
            value.extend,
        )
    elif isinstance(value, Gravity):
        value = Option('g', value.position, value.offset_x, value.offset_y)
    elif isinstance(value, DPR):
        value = Option('dpr', value.value)
    # Keep runtime validation for callers without static type checking.
    if not isinstance(value, Option):  # pyright: ignore[reportUnnecessaryIsInstance]
        raise TypeError('Unsupported processing option.')
    arguments = list(value.arguments)
    while arguments and arguments[-1] is EMPTY:
        arguments.pop()
    return ':'.join((value.name, *map(_argument, arguments)))


def _argument(value: Argument) -> str:
    if value is EMPTY:
        return ''
    if isinstance(value, bool):
        return str(int(value))
    return str(value)
