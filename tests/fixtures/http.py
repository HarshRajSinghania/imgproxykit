from collections.abc import Iterator

import pytest
import zapros


@pytest.fixture
def http_client() -> Iterator[zapros.Client]:
    """Provide an HTTP client with a timeout and automatic cleanup."""
    with zapros.Client() as client:
        yield client
