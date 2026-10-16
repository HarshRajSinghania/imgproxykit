import contextlib
import hashlib
import hmac

from imgproxykit.internal.urls import encode
from imgproxykit.types import EMPTY


class URLSigner:
    """Sign finalized paths or supply the unsigned URL marker."""

    __slots__ = ('_credentials',)

    def __init__(
        self,
        *,
        key: str | EMPTY = EMPTY,
        salt: str | EMPTY = EMPTY,
    ) -> None:
        """Decode a complete hex key/salt pair when supplied."""
        self._credentials: tuple[bytes, bytes] | None = None

        if key is EMPTY and salt is EMPTY:
            return
        if key is EMPTY or salt is EMPTY:
            raise ValueError('key and salt must be supplied together.')

        self._credentials = (
            _decode_hex(key, name='key'),
            _decode_hex(salt, name='salt'),
        )

    def __call__(self, path: str) -> str:
        """Return the signature for the exact supplied path."""
        if self._credentials is None:
            return 'unsafe'

        key, salt = self._credentials
        return encode(
            hmac.new(key, salt + path.encode(), hashlib.sha256).digest()
        )


def _decode_hex(value: str, *, name: str) -> bytes:
    with contextlib.suppress(ValueError):
        decoded = bytes.fromhex(value)
        if decoded:
            return decoded

    raise ValueError(f'Imgproxy {name} must be a nonempty hex string.')
