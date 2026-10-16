import pytest

from imgproxykit import options
from imgproxykit.internal.serialization import serialize_option


@pytest.mark.parametrize(
    ('option', 'expected'),
    [
        (options.AutoRotate(value=True), 'ar:1'),
        (options.AutoRotate(value=False), 'ar:0'),
        (options.EnforceThumbnail(value=True), 'eth:1'),
        (options.EnforceThumbnail(value=False), 'eth:0'),
        (options.Enlarge(value=True), 'el:1'),
        (options.Enlarge(value=False), 'el:0'),
        (options.KeepCopyright(value=True), 'kcr:1'),
        (options.KeepCopyright(value=False), 'kcr:0'),
        (options.PreserveHDR(value=True), 'ph:1'),
        (options.PreserveHDR(value=False), 'ph:0'),
        (options.Raw(value=True), 'raw:1'),
        (options.Raw(value=False), 'raw:0'),
        (options.ReturnAttachment(value=True), 'att:1'),
        (options.ReturnAttachment(value=False), 'att:0'),
        (options.StripColorProfile(value=True), 'scp:1'),
        (options.StripColorProfile(value=False), 'scp:0'),
        (options.StripMetadata(value=True), 'sm:1'),
        (options.StripMetadata(value=False), 'sm:0'),
    ],
)
def test_boolean_options(*, option: options.Option, expected: str) -> None:
    """Ensure that boolean options serialize enabled and disabled values."""
    assert serialize_option(option) == expected
