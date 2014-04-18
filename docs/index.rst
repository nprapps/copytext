==================
copytext |release|
==================

About
=====

.. include:: ../README

Installation
============

Users
-----

If you only want to use copytext, install it this way::

    pip install copytext

Developers
----------

If you are a developer that also wants to hack on copytext, install it this way::

    git clone git://github.com/nprapps/copytext.git
    cd copytext
    mkvirtualenv --no-site-packages copytext
    pip install -r requirements.txt
    python setup.py develop
    nosetests

Usage
=====

::

    import copytext

    # Instantiate our copy, this parses the XLSX workbook
    copy = copytext.Copy('examples/test_copy.xlsx')

    # Get a sheet named "content"
    sheet = copy['content']

    # The sheet has "key" and "value" columns
    # This tells copytext to access the value by the key 

    # Print the value where the "key" is named "lorem_ipsum"
    print sheet['lorem_ipsum']

    # Print the value in the third row (counting headers)
    print sheet[2]

    # The rows themselves are also objects
    row = sheet['lorem_ipsum']
    
    # You can access the columns by indexing into the row

    # Print the key column of the row
    print row['key']

    # Print the first column in the row
    print row[0]

    # You can also iterate over rows
    for row in sheet:
        # Print the value
        print row

        # Print the key/value pair
        print row['key'], row['value']

    # This sheet has "term" and "definition" columns, but no "key"
    sheet = copy['example_list']

    # This won't work
    # print sheet[0]

    # But this will
    for row in sheet:
        print row['term'], row['definition']

    # You can have as many rows and columns as you want!

.. note::

    Copytext only understands **xlsx** files, and all cells must be converted to text formatting. Copytext does not grok dates or numbers.

License
=======

.. include:: ../COPYING

Changelog
=========

.. include:: ../CHANGELOG

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

