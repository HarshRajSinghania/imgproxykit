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
