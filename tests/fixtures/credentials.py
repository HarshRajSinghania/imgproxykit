from typing import final

import pytest
from typing_extensions import TypedDict


@final
class Credentials(TypedDict, closed=True):
    """Hexadecimal credentials accepted by clients and URL signers."""

    key: str
    salt: str


@pytest.fixture(scope='session')
def credentials() -> Credentials:
    """Provide the signing credentials shared with the imgproxy server."""
    return {
        'key': '736563726574',
        'salt': '73616c74',
    }
