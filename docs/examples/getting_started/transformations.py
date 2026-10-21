"""
Resize an image and select its output format.

>>> url.split('/unsafe/')[1].split('/')[0:2]
['resize:fill:300:300', 'format:webp']
"""

from imgproxykit import Client, Transform
from imgproxykit.options import Resize

client = Client('https://imgproxykit.url.com')
image = 'https://example.com/photo.jpg'
thumbnail = Transform(
    Resize(width=300, height=300, mode='fill'),
    format='webp',
)

url = client.url(image, transform=thumbnail)
