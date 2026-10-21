"""
Leave processing options to the server.

>>> default_url == none_url == empty_url
True
>>> default_url
'https://imgproxykit.url.com/unsafe/aHR0cHM6Ly9leGFtcGxlLmNvbS9waG90by5qcGc'
"""

from imgproxykit import Client, Transform

client = Client('https://imgproxykit.url.com')
image = 'https://example.com/photo.jpg'

default_url = client.url(image)
none_url = client.url(image, transform=None)
empty_url = client.url(image, transform=Transform())
