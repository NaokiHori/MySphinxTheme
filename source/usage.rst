#####
Usage
#####

In your existing Sphinx project, put `mysphinxtheme <https://github.com/NaokiHori/MySphinxTheme/tree/main/source/mysphinxtheme>`_ directory under the ``source`` directory (i.e. same place as ``conf.py``), e.g.:

.. code-block:: console
   :caption: Example structre

   source
   ├── conf.py
   ├── index.rst
   ├── mysphinxtheme
   │  ├── layout.html
   │  ├── page.html
   │  ├── static
   │  │  ├── content.css
   │  │  ├── footer.css
   │  │  ├── header.css
   │  │  ├── mysphinxtheme.css
   │  │  └── toctree.css
   │  ├── support.py
   │  └── theme.conf
   ├── your-doc-1.rst
   └── your-doc-2.rst

Add the following lines to your ``conf.py`` so that Sphinx builder knows this theme is to be used:

.. code-block:: python
   :caption: conf.py

   html_theme = "mysphinxtheme"
   html_theme_path = ["."]

If the current directory is not included in your PATH, add the following as well:

.. code-block:: python
   :caption: conf.py

   import os
   import sys

   sys.path.append(os.path.abspath("."))

Optionally, you can display a short description of your project and can provide a hyperlink to your GitHub repository in the headers by adding

.. code-block:: python
   :caption: conf.py

   html_theme_options = {
           "description": "A short description",
           "github_repo": "https://github.com/Your/GitHubRepository",
   }

Then build the document as usual:

.. code-block:: console
   :caption: console

   sphinx-build -M html source build

For your reference, here is the ``conf.py`` I use to build *this* document:

.. literalinclude:: conf.py
   :language: python
   :linenos:

