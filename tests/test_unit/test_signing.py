from typing import Final

import pytest

from imgproxykit.signing import URLSigner
from imgproxykit.types import EMPTY

_KEY: Final = '736563726574'
_SALT: Final = '73616c74'


@pytest.mark.parametrize('path', ['/', '/image.jpg'])
def test_unsigned_path(*, path: str) -> None:
    """Ensure that omitted credentials select the unsafe marker."""
    assert URLSigner()(path) == 'unsafe'


@pytest.mark.parametrize(
    ('path', 'expected'),
    [
        (
            '/rs:fill:300:200/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc.webp',
            'IFOHEnjwIOnwbBU8WexRy_3nv99lVipxJG_F6tiWiKY',
        ),
        (
            '/café/naïve.jpg',
            'ZN61oYlsd53IQaf_0-oqrAi9eBYyCLJrkYNriTUOkGE',
        ),
        ('/a/../b', 'CSsxSKjH31lwRHIcZ_mhhYmN0Z-Wj8nbQP5x8qDc_F8'),
        ('/b', 'pEIkEjcNKr42hrTpB8MBu9UnfgKo7uw7t_x-6he7lc8'),
    ],
)
def test_signed_path(*, path: str, expected: str) -> None:
    """Ensure that the exact UTF-8 path matches independent test vectors."""
    # Vectors use OpenSSL HMAC-SHA256 with key b'secret' and salt b'salt'.
    signer = URLSigner(key=_KEY, salt=_SALT)

    assert signer(path) == expected


def test_signer_reuse() -> None:
    """Ensure that signing another path does not change previous signatures."""
    signer = URLSigner(key=_KEY, salt=_SALT)

    assert signer('/b') == 'pEIkEjcNKr42hrTpB8MBu9UnfgKo7uw7t_x-6he7lc8'
    assert signer('/a/../b') == 'CSsxSKjH31lwRHIcZ_mhhYmN0Z-Wj8nbQP5x8qDc_F8'
    assert signer('/b') == 'pEIkEjcNKr42hrTpB8MBu9UnfgKo7uw7t_x-6he7lc8'


@pytest.mark.parametrize(
    ('key', 'salt'),
    [('00', _SALT), (_KEY, '00')],
)
def test_different_credentials(*, key: str, salt: str) -> None:
    """Ensure that both the key and salt affect the signature."""
    signer = URLSigner(key=_KEY, salt=_SALT)

    assert URLSigner(key=key, salt=salt)('/b') != signer('/b')


@pytest.mark.parametrize('salt', [_SALT, _SALT.upper()])
def test_uppercase_credentials(*, salt: str) -> None:
    """Ensure that hexadecimal credentials are case insensitive."""
    signer = URLSigner(key='ABCDEF', salt=salt)

    assert signer('/b') == URLSigner(key='abcdef', salt=_SALT)('/b')


@pytest.mark.parametrize(
    ('key', 'salt'),
    [
        (_KEY, EMPTY),
        (EMPTY, _SALT),
    ],
)
def test_incomplete_credentials(*, key: str | EMPTY, salt: str | EMPTY) -> None:
    """Ensure that signing requires both credentials together."""
    with pytest.raises(
        ValueError,
        match='key and salt must be supplied together',
    ):
        URLSigner(key=key, salt=salt)


@pytest.mark.parametrize('invalid', ['', '   ', 'invalid', '0'])
@pytest.mark.parametrize('credential', ['key', 'salt'])
def test_invalid_credentials(*, invalid: str, credential: str) -> None:
    """Ensure that either credential rejects empty or invalid hex data."""
    credentials = {'key': _KEY, 'salt': _SALT}
    credentials[credential] = invalid

    with pytest.raises(
        ValueError,
        match='Signing credentials must be nonempty hex strings',
    ):
        URLSigner(**credentials)
