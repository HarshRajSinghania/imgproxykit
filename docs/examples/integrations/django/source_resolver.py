"""
Resolve relative image URLs against a media domain.

>>> resolve_image_source('/media/photo.jpg')
'https://media.example.com/media/photo.jpg'
>>> resolve_image_source('https://storage.example.com/photo.jpg')
'https://storage.example.com/photo.jpg'
"""

from urllib.parse import urljoin

from django.db.models.fields.files import FieldFile


def resolve_image_source(source: str | FieldFile) -> str:
    """Return an absolute source URL for a string or model file field."""
    url = source.url if isinstance(source, FieldFile) else source
    return urljoin('https://media.example.com/', url)
