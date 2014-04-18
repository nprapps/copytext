#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import unittest2 as unittest

import copytext

class CopyTestCase(unittest.TestCase):
    """
    Test the Copy object.
    """
    def setUp(self):
        self.copy = copytext.Copy('examples/test_copy.xlsx')

    def test_sheet_by_item_name(self):
        sheet = self.copy['content']
        self.assertTrue(isinstance(sheet, copytext.Sheet))

    def test_sheet_by_prop_name(self):
        with self.assertRaises(AttributeError):
            self.copy.content

    def test_sheet_does_not_exist(self):
        error = self.copy['foo']
        self.assertTrue(isinstance(error, copytext.Error))
        self.assertEquals(error._error, 'COPY.foo [sheet does not exist]')

    def test_json(self):
        s = self.copy.json()
        data = json.loads(s)
    
        self.assertTrue('attribution' in data)
        self.assertTrue('content' in data)
        self.assertTrue('example_list' in data)

        attribution = data['attribution']

        self.assertIsInstance(attribution, dict)
        self.assertTrue('byline' in attribution)
        self.assertEqual(attribution['byline'], u'Uñicodë')

        example_list = data['example_list']

        self.assertIsInstance(example_list, list)
        self.assertIsInstance(example_list[0], list)
        self.assertEqual(example_list[0], ['term', 'definition'])

class SheetTestCase(unittest.TestCase):
    """
    Test the Sheet object.
    """
    def setUp(self):
        copy = copytext.Copy('examples/test_copy.xlsx')
        self.sheet = copy['content']

    def test_row_by_key_item_index(self):
        row = self.sheet[1]
        self.assertTrue(isinstance(row, copytext.Row))

    def test_row_by_key_item_name(self):
        row = self.sheet['header_title']
        self.assertTrue(isinstance(row, copytext.Row))

    def test_row_by_key_prop_name(self):
        with self.assertRaises(AttributeError):
            self.sheet.header_title

    def test_key_does_not_exist(self):
        error = self.sheet['foo']
        self.assertTrue(isinstance(error, copytext.Error))
        self.assertEquals(error._error, 'COPY.content.foo [key does not exist in sheet]')

    def test_column_index_outside_range(self):
        error = self.sheet[65]
        self.assertTrue(isinstance(error, copytext.Error))
        self.assertEquals(error._error, 'COPY.content.65 [row index outside range]')

class RowTestCase(unittest.TestCase):
    """
    Test the Row object.
    """
    def setUp(self):
        copy = copytext.Copy('examples/test_copy.xlsx')
        sheet = copy['content']
        self.row = sheet['header_title']

    def test_cell_by_value_repr(self):
        cell = repr(self.row)
        self.assertTrue(isinstance(cell, basestring))
        self.assertEqual(cell, 'Across-The-Top Header')

    def test_cell_by_index(self):
        cell = self.row[1]
        self.assertTrue(isinstance(cell, basestring))
        self.assertEqual(cell, 'Across-The-Top Header')

    def test_cell_by_item_name(self):
        cell = self.row['value']
        self.assertTrue(isinstance(cell, basestring))
        self.assertEqual(cell, 'Across-The-Top Header')

    def test_cell_by_prop_name(self):
        with self.assertRaises(AttributeError):
            self.row.value

    def test_column_does_not_exist(self):
        error = self.row['foo']
        self.assertTrue(isinstance(error, copytext.Error))
        self.assertEquals(error._error, 'COPY.content.1.foo [column does not exist in sheet]')

    def test_column_index_outside_range(self):
        error = self.row[2]
        self.assertTrue(isinstance(error, copytext.Error))
        self.assertEquals(error._error, 'COPY.content.1.2 [column index outside range]')

class CellTypeTestCase(unittest.TestCase):
    """
    Test various cell "types".

    NB: These tests are fake. They only work if the input data is formatted as text.

    Things which are actually non-string don't work and can't be supported.
    """
    def setUp(self):
        copy = copytext.Copy('examples/test_copy.xlsx')
        self.sheet = copy['attribution']

    def test_date(self):
        row = self.sheet['pubdate']
        val = repr(row)

        self.assertEquals(val, '1/22/2013')

    def test_time(self):
        row = self.sheet['pubtime']
        val = repr(row)

        self.assertEqual(val, '3:37 AM')

class DummyCellWrapper(unicode):
    """
    Example of a cell wrapper class. A psuedo-implementation
    of Flask's Markup class.
    """
    def __new__(cls, text):
        self = super(DummyCellWrapper, cls).__new__(cls, text)

        return self

    def __html__(self):
        return u'<strong>%s</strong>' % self 

class CellWrapperTestCase(unittest.TestCase):
    """
    Test the optional cell filter.
    """
    def setUp(self):
        copy = copytext.Copy('examples/test_copy.xlsx', cell_wrapper_cls=DummyCellWrapper)
        sheet = copy['content']
        self.row = sheet['header_title']

    def test_wrapper_applied(self):
        cell = self.row['value']

        self.assertTrue(isinstance(cell, DummyCellWrapper))
        self.assertTrue(isinstance(cell, unicode))
        self.assertEqual(cell, 'Across-The-Top Header')
        self.assertEqual(cell.__html__(), '<strong>Across-The-Top Header</strong>')

class ErrorTestCase(unittest.TestCase):
    """
    Test for Error object.
    """
    def setUp(self):
        self.error = copytext.Error('foobar')

    def test_getitem(self):
        child_error = self.error['bing']
        self.assertIs(child_error, self.error)
        self.assertEqual(str(child_error), 'foobar')

    def test_getitem_index(self):
        child_error = self.error[1]
        self.assertIs(child_error, self.error)
        self.assertEqual(str(child_error), 'foobar')

    def test_iter(self):
        i = iter(self.error)
        child_error = i.next()
        self.assertIs(child_error, self.error)
        self.assertEqual(str(child_error), 'foobar')

        with self.assertRaises(StopIteration):
            i.next()

    def test_len(self):
        self.assertEqual(len(self.error), 1)

    def test_repr(self):
        self.assertEqual(str(self.error), 'foobar')
