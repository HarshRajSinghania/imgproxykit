from imgproxykit.internal.encoding import encode_base64
from imgproxykit.types import EMPTY


def build_path(
    source: str,
    *,
    options: tuple[str, ...],
    output_format: str | EMPTY = EMPTY,
) -> str:
    """
    Assemble serialized options, an encoded source, and an output extension.

    The leading ``/`` is part of the path supplied to the signer.
    The source is encoded as URL-safe Base64 without padding. An omitted
    output format adds no extension, leaving format selection to imgproxy.

    """
    segments = '/'.join((*options, encode_base64(source)))
    path = f'/{segments}'
    return path if output_format is EMPTY else f'{path}.{output_format}'
