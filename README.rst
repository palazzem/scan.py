=======
Scan.py
=======

A simple scanner wrapper, built on top of `scanimage (SANE)`_, and `imagemagick`_.

The scanning process involves the following steps:

* Scan a paper using ``scanimage``
* Proceed with the first step until done (batch scan)
* Compress all images (``TIFF``) into ``JPEG`` format
* Merge all ``JPEG`` images into a single ``PDF`` file

Implementation
--------------

This implementation is really simple and doesn't provide a full set of features that you
will normally have using these tools manually. I just need these configurations and I wrote
this script just to scan quickly some papers.

Requirements
------------

``Scan.py`` works only if the following packages are installed in your system:

* `scanimage (SANE)`_
* `imagemagick`_

Roadmap
-------

* make the script a little more generic
* provide a simple CLI interface

License
-------

``Scan.py`` is released under the terms of the **BSD LICENSE**. Full details in ``LICENSE`` file.

.. _scanimage (SANE): http://www.sane-project.org/
.. _imagemagick: http://www.imagemagick.org/
