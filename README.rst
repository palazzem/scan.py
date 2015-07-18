=======
Scan.py
=======

A simple scanner wrapper, built on top of `scanimage (SANE)`_, and `imagemagick`_.

The scanning process involves the following steps:

* Scan a paper using ``scanimage``
* Proceed with the first step until done (batch scan)
* Compress all images (``TIFF``) into ``JPEG`` format
* Merge all ``JPEG`` images into a single ``PDF`` file

Requirements
------------

``Scan.py`` works only if the following packages are installed in your system:

* `scanimage (SANE)`_
* `imagemagick`_

License
-------

``Scan.py`` is released under the terms of the **BSD LICENSE**. Full details in ``LICENSE`` file.

.. _scanimage (SANE): http://www.sane-project.org/
.. _imagemagick: http://www.imagemagick.org/
