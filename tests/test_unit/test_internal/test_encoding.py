import pytest

from imgproxykit.internal.encoding import encode_base64


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        # Empty input:
        ('', ''),
        (b'', ''),
        # Two, one, and no padding characters:
        ('f', 'Zg'),
        ('fo', 'Zm8'),
        ('foo', 'Zm9v'),
        # Text is encoded as UTF-8:
        ('café', 'Y2Fmw6k'),
        # Binary input uses the URL-safe alphabet:
        (b'\xfb\xef', '--8'),
        (b'\xff\xff', '__8'),
    ],
)
def test_encode_base64(*, value: str | bytes, expected: str) -> None:
    """Ensure that text and bytes use URL-safe Base64 without padding."""
    assert encode_base64(value) == expected
