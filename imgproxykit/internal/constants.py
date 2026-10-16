from typing import Final

# imgproxy verifies URL signatures using HMAC-SHA256.
SIGNATURE_DIGEST: Final = 'sha256'
# A URL still needs a signature segment when server signature checking is off.
UNSAFE: Final = 'unsafe'
# imgproxy's short option name for referencing server-side presets.
PRESET: Final = 'pr'
