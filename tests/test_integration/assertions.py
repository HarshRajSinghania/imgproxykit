from http import HTTPStatus
from io import BytesIO

from PIL import Image
from zapros import Response

type Position = tuple[int, int]
type Color = tuple[int, int, int]


def assert_image(
    response: Response,
    *,
    format: str,  # noqa: A002
    size: tuple[int, int],
    pixels: dict[Position, Color] | None = None,
) -> None:
    """Ensure that a successful response contains the expected image."""
    assert response.status == HTTPStatus.OK, response.text
    with Image.open(BytesIO(response.read())) as image:
        image.load()
        assert image.format == format
        assert image.size == size
        assert response.headers['Content-Type'] == Image.MIME[format]

        with image.convert('RGB') as rgb_image:
            for position, color in (pixels or {}).items():
                assert rgb_image.getpixel(position) == color, position
