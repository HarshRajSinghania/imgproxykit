<h1 align="center">imgproxykit</h1>

<p align="center">
  <em>A typed Python toolkit for building imgproxy URLs.</em>
</p>

<p align="center">
  <a href="#features">Features</a> ·
  <a href="#installation">Installation</a> ·
  <a href="#example">Example</a> ·
  <a href="https://github.com/kondratevdev/imgproxykit/issues">Issues</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

Define image transformations in Python and turn them into reusable, signed URLs.
Your imgproxy server fetches and processes the image when the URL is requested.

## Features

- [x] Typed API with annotations
- [x] Immutable, reusable transforms built from Python dataclasses
- [x] Free imgproxy processing options, including geometry, filters, metadata,
      quality, pixel density, gravity, and watermarks
- [x] Output format selection, including WebP and AVIF
- [x] Support for named presets configured on your imgproxy server

## Installation

Requires **Python 3.12+** and a running imgproxy server.

```bash
pip install imgproxykit
```

## Example

Create a client, define a transform, and generate a URL:

```pycon
>>> from imgproxykit import Client, Transform
>>> from imgproxykit.options import Quality, Resize
>>> client = Client('https://images.example.com')
>>> thumbnail = Transform(
...     options=(
...         Resize(width=300, height=300, mode='fill'),
...         Quality(85),
...     ),
...     format='webp',
... )
>>> url = client.url(
...     'https://example.com/photo.jpg',
...     transform=thumbnail,
... )
>>> url.startswith('https://images.example.com/unsafe/rs:fill:300:300/q:85/')
True
>>> url.endswith('.webp')
True

```

Reuse `client` and `thumbnail` for other source images. Options you omit are
left to imgproxy's defaults.

Without signing credentials, URLs use the `unsafe` marker and require a server
with signature checking disabled.

### Signed URLs

Supply the hex-encoded key and salt from your imgproxy server configuration:

```python
import os

from imgproxykit import Client

client = Client(
    'https://images.example.com',
    key=os.environ['IMGPROXY_KEY'],
    salt=os.environ['IMGPROXY_SALT'],
)

url = client.url(
    'https://example.com/photo.jpg',
    transform=thumbnail,
)
```

Both credentials are required together. The client signs each generated path
automatically.

### Server presets

Already have presets on your imgproxy server? Reference them by name:

```python
url = client.url(
    'https://example.com/photo.jpg',
    presets=('thumbnail', 'watermarked'),
    format='webp',
)
```

Use either a Python `transform` or server `presets` in each call.
For Python transforms, set `format` on `Transform`; for presets, pass it to
`client.url()`.

## Contributing

See the [contributing guide](CONTRIBUTING.md) for development setup and checks.
Bug reports and feature requests are welcome on the
[issue tracker](https://github.com/kondratevdev/imgproxykit/issues).

## License

[MIT](LICENSE)

## Credits

Generated with
[`wemake-python-package`](https://github.com/wemake-services/wemake-python-package)
([template version](https://github.com/wemake-services/wemake-python-package/tree/47d9dddd29da8d6d3d1a403f8a143b323a812083)).
