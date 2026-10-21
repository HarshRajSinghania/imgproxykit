"""
Use a deployment path prefix and a source URI.

>>> url
'https://imgproxykit.url.com/imgproxy/unsafe/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
"""

from imgproxykit import Client

client = Client('https://imgproxykit.url.com/imgproxy/')
image = 'https://example.com/photo.jpg'
url = client.url(image)
