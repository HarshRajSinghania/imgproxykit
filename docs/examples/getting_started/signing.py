"""
Sign a URL with example credentials.

>>> url.startswith('https://imgproxykit.url.com/unsafe/')
False
>>> url == client.url(image)
True
"""

from imgproxykit import Client

client = Client(
    'https://imgproxykit.url.com',
    key='736563726574',
    salt='73616c74',
)
image = 'https://example.com/photo.jpg'

url = client.url(image)
