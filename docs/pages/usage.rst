Usage
=====

Signed URLs
-----------

Use the same hex-encoded key and salt as your imgproxy server. These fixed
credentials are for examples only::

    >>> from imgproxykit import Client
    >>> client = Client(
    ...     'https://images.example.com',
    ...     key='736563726574',
    ...     salt='73616c74',
    ... )
    >>> url = client.url('https://example.com/photo.jpg')
    >>> url.startswith('https://images.example.com/unsafe/')
    False
    >>> url == client.url('https://example.com/photo.jpg')
    True
