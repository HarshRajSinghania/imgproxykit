from imgproxykit.options import Option
from imgproxykit.types import EMPTY, Argument


def serialize_option(option: Option) -> str:
    """Serialize a typed processing option into an imgproxy path segment."""
    return serialize_segment(option.name, option.arguments)


def serialize_segment(name: str, arguments: tuple[Argument, ...]) -> str:
    """
    Serialize an option name and positional arguments into a path segment.

    Internal :data:`~imgproxykit.types.EMPTY` values become empty positions;
    trailing empty values are omitted. Explicit zeroes and empty strings
    retain their positions. Booleans are serialized as ``1`` and ``0``.

    """
    end = len(arguments)
    while end and arguments[end - 1] is EMPTY:
        end -= 1
    return ':'.join((name, *map(_serialize_argument, arguments[:end])))


def _serialize_argument(value: Argument) -> str:
    """Serialize one argument without treating false values as omitted."""
    if value is EMPTY:
        return ''
    if isinstance(value, bool):
        return str(int(value))
    return str(value)
