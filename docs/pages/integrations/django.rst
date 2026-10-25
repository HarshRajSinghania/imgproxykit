Django
======

Generate imgproxy URLs from source strings and model file fields in Python
code or Django templates. Configure the client and reusable transformations
in Django settings, then generate individual image URLs or named sets of
image variants.

Installation
------------

.. md-tab-set::

  .. md-tab-item:: :iconify:`material-icon-theme:uv` uv

    .. code-block:: bash

      uv add 'imgproxykit[django]'

  .. md-tab-item:: :iconify:`devicon:poetry` poetry

    .. code-block:: bash

      poetry add 'imgproxykit[django]'

  .. md-tab-item:: :iconify:`devicon:pypi` pip

    .. code-block:: bash

      pip install 'imgproxykit[django]'

To use template tags, add the integration to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'imgproxykit.integrations.django',
    ]

.. tip::

    Adding the integration to ``INSTALLED_APPS`` is only required for template
    tags.

Configuration
-------------

Define ``IMGPROXYKIT`` in your Django settings:

.. literalinclude:: /examples/integrations/django/settings.py
   :language: python
   :start-at: from

``client.base_url`` is required. Set ``key`` and ``salt`` to your server's
hex-encoded credentials, or omit both if the server accepts unsigned URLs.
See :doc:`../user-guide/client` for other client options.

``transforms`` defines named transformations, and ``variants`` groups
transformations into named sets. Both are optional and can be reused by
Python shortcuts and template tags.

Generate URLs
-------------

Use ``imgproxy_url`` with a source string or model file field and a
transformation name from ``IMGPROXYKIT['transforms']``:

.. TODO: Move this code block to docs/examples/integrations/django/url.py.

.. code-block:: python

    from imgproxykit.integrations.django import imgproxy_url

    source = 'https://media.example.com/products/42.jpg'
    image_url = imgproxy_url(source, 'thumbnail')

You can also pass a ``Transform`` object directly. Omit the transformation
argument to generate a URL without processing options.

Generate variants
-----------------

Use ``imgproxy_variants`` with a set name from ``IMGPROXYKIT['variants']``
to generate several URLs for the same source:

.. TODO: Move this code block to docs/examples/integrations/django/variants.py.

.. code-block:: python

    from imgproxykit.integrations.django import imgproxy_variants

    source = 'https://media.example.com/products/42.jpg'
    images = imgproxy_variants(source, 'product')

    preview_url = images['small']
    large_url = images['large']

The result is a dictionary of URLs with the configured variant names as keys.
You can also pass a dictionary of names and ``Transform`` objects directly
instead of a set name.

Templates
---------

.. warning::

    Add ``'imgproxykit.integrations.django'`` to ``INSTALLED_APPS`` before
    using the template tags.

Load ``imgproxykit`` in your template, then use ``imgproxy_url`` to display
an image with the ``thumbnail`` transformation configured above:

.. code-block:: django

    {% load imgproxykit %}

    <img src="{% imgproxy_url product.image 'thumbnail' %}" alt="{{ product.name }}">

The source can be a model file field, as shown here, or a source string.
The transformation name is optional; omitting it generates a URL without
processing options.

For a preview that links to a larger image, use ``imgproxy_variants`` with
the configured ``product`` variant set:

.. code-block:: django

    {% load imgproxykit %}
    {% imgproxy_variants product.image 'product' as images %}

    <a href="{{ images.large }}">
      <img src="{{ images.small }}" alt="{{ product.name }}">
    </a>

Source resolution
-----------------

When generating URLs in Python or templates, imgproxykit passes source
strings unchanged and reads ``.url`` from model file fields.

In Django, a file field's URL depends on the storage backend and its
configuration. It may be relative, such as ``/media/photo.jpg``, or absolute,
such as ``https://media.example.com/photo.jpg``. imgproxykit does not expand
relative URLs automatically.

To use relative URLs, you can configure `IMGPROXY_BASE_URL
<https://docs.imgproxy.net/latest/configuration/options#source-image-urls>`__
on your imgproxy server. For example, with
``IMGPROXY_BASE_URL=https://media.example.com``, imgproxy fetches
``/media/photo.jpg`` from ``https://media.example.com/media/photo.jpg``.
This setting adds a prefix to source URLs unless they already contain it.

Alternatively, override source resolution in Django with
``IMGPROXYKIT['source_resolver']``. The resolver receives the original string
or file field and must return a URI that your imgproxy server can access.
For example, add a media domain in ``myapp/images.py``:

.. literalinclude:: /examples/integrations/django/source_resolver.py
   :language: python
   :start-at: from urllib.parse

Register the resolver in your Django settings:

.. code-block:: python

    IMGPROXYKIT = {
        # ...
        'source_resolver': 'myapp.images.resolve_image_source',
    }

This turns ``/media/photo.jpg`` into
``https://media.example.com/media/photo.jpg`` and leaves absolute URLs
unchanged. The setting also accepts a callable directly instead of an
import path.

Next steps
----------

* :doc:`../user-guide/transformations` describes reusable transformations.
* :doc:`../user-guide/variants` shows how to generate several image URLs.
* :doc:`../api-reference/django` documents the client, URL generation functions,
  source resolution, and settings.
