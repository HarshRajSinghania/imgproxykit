import base64


def encode_base64(value: str | bytes) -> str:
    """
    Encode text or bytes as URL-safe Base64 without padding.

    Text is first encoded as UTF-8. Byte values, such as signature digests,
    are encoded directly. Trailing ``=`` padding is removed for URL paths.

    """
    raw = value.encode() if isinstance(value, str) else value
    return base64.urlsafe_b64encode(raw).rstrip(b'=').decode()
