# Version history

We will follow [Semantic Versions](https://semver.org/) since `1.0.0` release.
While in `Development Status :: 3 - Alpha` - we will break
all the things without any notices.

After `Development Status :: 4 - Beta` we will still break things
but with a deprecation period.


## 0.3.0 WIP

### Features

- `Expires` now accepts timezone-aware `datetime` and `timedelta` values in addition to Unix timestamps. Values are normalized to a timestamp at construction time so transforms remain reusable. Naive datetimes are rejected, #43

### Breaking changes

- `Preset` now takes preset names as positional arguments, so
  `Preset('thumbnail', 'watermarked')` replaces
  `Preset(names=('thumbnail', 'watermarked'))`. Supplied names keep their
  order, #27
- Added `arguments_separator` parameter to `Client` and `PathSerializer`
  to match `IMGPROXY_ARGUMENTS_SEPARATOR`, defaults to `:`. 
  `Client` now passes it to `path_serializer_cls`, so custom path serializer
  constructors must accept this keyword argument, #26

## 0.2.1

### Breaking changes

- Replaced the `presets` argument of `Client.url` and `PathBuilder`
  with the `Preset` option, which can be combined with other
  processing options in `Transform`, #12
- Removed the `format` argument of `Client.url`, the `output_format`
  argument of `PathBuilder`, and the `Transform.format` attribute.
  Use `Transform(Format('webp'))` or `Transform(format='webp')` instead.
  Output formats are now serialized as processing options,
  like `format:webp`, instead of source URL extensions, #12 and #18
- `Transform` now accepts option instances as positional arguments
  instead of an `options` tuple. Replace
  `Transform(options=(Resize(width=300), Quality(85)))`
  with `Transform(Resize(width=300), Quality(85))`, #14
- Removed `imgproxykit.builders.PathBuilder`, use
  `imgproxykit.serialization.PathSerializer` instead, #14

### Features

- Added `Client` constructor arguments for signing key and salt, #12
- Added support for signed URLs with `Client.url(..., sign=True)`, #12

## 0.2.0

### Breaking changes

- Renamed package from `imgproxy` to `imgproxykit`, #1

### Features

- Initial public release with typed options and URL builder, #1

## Version 0.1.0

- Initial release
