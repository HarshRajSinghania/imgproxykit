from typing_extensions import Sentinel

# NOTE: this module must not import anything from `imgproxykit`,
# so it can be used anywhere without creating import cycles.

#: Default singleton for empty values.
#: Re-exported as ``imgproxykit.types.EMPTY``.
EMPTY = Sentinel('EMPTY')
