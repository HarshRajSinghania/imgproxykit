"""
Customize the unsigned URL marker.

>>> url.split('/')[3]
'public'
"""

from imgproxykit import Client

client = Client(
    'https://imgproxykit.url.com',
    unsigned_signature='public',
)
url = client.url('https://example.com/photo.jpg')
