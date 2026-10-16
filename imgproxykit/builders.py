from imgproxykit.internal.urls import build_path, serialize_option
from imgproxykit.options import Option
from imgproxykit.transform import Transform
from imgproxykit.types import EMPTY


class PathBuilder:
    """Resolve processing parameters and assemble the unsigned URL path."""

    __slots__ = ()

    def __call__(
        self,
        source: str,
        *,
        transform: Transform | EMPTY = EMPTY,
        presets: tuple[str, ...] | EMPTY = EMPTY,
        output_format: str | EMPTY = EMPTY,
    ) -> str:
        """Build a path from a Python transform or server preset names."""
        selected = self._resolve_transform(transform, presets, output_format)
        return build_path(
            source,
            options=tuple(
                serialize_option(option) for option in selected.options
            ),
            output_format=selected.format,
        )

    def _resolve_transform(
        self,
        transform: Transform | EMPTY,
        presets: tuple[str, ...] | EMPTY,
        output_format: str | EMPTY,
    ) -> Transform:
        if presets is not EMPTY:
            if transform is not EMPTY:
                raise ValueError('Choose transform or presets.')
            return Transform(
                options=(Option('pr', *presets),), format=output_format
            )
        if output_format is not EMPTY:
            raise ValueError('Set format on the Python transform.')
        return Transform() if transform is EMPTY else transform
