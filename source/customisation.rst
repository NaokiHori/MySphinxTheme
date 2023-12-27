#############
Customisation
#############

This theme only contains the following.

**********
HTML files
**********

Under ``mysphinxtheme``, there are two HTML files: ``layout.html`` and ``page.html``.
``layout.html`` plays the central role to construct each page and is to be modified accordingly if you want to make changes (e.g. add a sidebar).
``page.html`` is merely a wrapper and you do not have to touch in general.

Note that templating by `Jinja <https://palletsprojects.com/p/jinja/>`_ is adopted to handle variables.

************
Style sheets
************

By default, the ``layout.html`` consists of four elements: a header, main contents provided by the *reStructuredText* files, a table-of-contents tree, and a footer.
Each element has its own style sheets under ``mysphinxtheme/static/``.
General configurations are given by the additional file ``mysphinxtheme/static/mysphinxtheme.css``.

**************
Pygments style
**************

Sphinx uses `Pygments <https://pygments.org>`_ to highlight code blocks, whose colors are offered by a python script ``mysphinxtheme/support.py``.
Modify it accordingly if you want to change the color scheme of the code blocks.

*******************
Theme configuration
*******************

To be minimal, I include only two options to change the final appearance.
You can add several options and customise the HTML templates accordingly.

