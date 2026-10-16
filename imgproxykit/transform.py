from dataclasses import dataclass

from imgproxykit.options import Option
from imgproxykit.types import EMPTY, FormatType


@dataclass(frozen=True, slots=True, kw_only=True)
class Transform:
    """
    Define reusable image processing options and an optional output format.

    Instances are immutable and can be reused for multiple source images
    and clients. Pass a transform to :meth:`imgproxykit.Client.url` to
    include its processing options and output format in the generated URL.

    Options are serialized in the supplied order. imgproxy determines the
    image processing pipeline and resolves omitted option arguments using
    its defaults. Creating a transform does not process an image or make
    a network request.

    Attributes:
        options: Tuple of typed processing options. Defaults to an empty
            tuple, which adds no processing option segments to the URL.
        format: Output image format, such as ``webp`` or ``avif``.
            Defaults to :data:`~imgproxykit.types.EMPTY`, leaving format
            selection to imgproxy.

    Usage:

    >>> from imgproxykit import Client, Transform
    >>> from imgproxykit.options import Quality, Resize
    >>> thumbnail = Transform(
    ...     options=(
    ...         Resize(width=300, height=300, mode='fill'),
    ...         Quality(85),
    ...     ),
    ...     format='webp',
    ... )
    >>> client = Client('https://images.example.com')
    >>> first_url = client.url(
    ...     'https://example.com/first.jpg',
    ...     transform=thumbnail,
    ... )
    >>> second_url = client.url(
    ...     'https://example.com/second.jpg',
    ...     transform=thumbnail,
    ... )

    """

    # TODO: Add immutable composition; define duplicate option handling,
    # format overrides, and explicitly clearing an inherited format.
    options: tuple[Option, ...] = ()
    format: FormatType | EMPTY = EMPTY
