from abc import ABC, abstractmethod
from typing import ClassVar

from imgproxykit.types import Argument, OptionType


class Option(ABC):
    """
    Base class for typed imgproxy processing options.

    Concrete options provide a fixed name and positional arguments.
    Pass their instances to :class:`~imgproxykit.Transform`.
    This abstract class cannot be instantiated directly.

    Arguments retain :data:`~imgproxykit.types.EMPTY` values until
    serialization: internal gaps keep their positions, while trailing
    empty arguments are omitted.

    See `imgproxy processing options
    <https://docs.imgproxy.net/usage/processing#processing-options>`_.

    """

    __slots__ = ()

    # TODO: Define runtime validation boundaries for processing option values.
    # TODO: Allow custom option names without type ignores; decide whether
    # OptionType should remain limited to built-in processing options.

    # Private API:
    _name: ClassVar[OptionType]

    @property
    def name(self) -> OptionType:
        """The fixed imgproxy processing option name."""
        return self._name

    @property
    @abstractmethod
    def arguments(self) -> tuple[Argument, ...]:
        """Positional arguments in imgproxy protocol order."""
