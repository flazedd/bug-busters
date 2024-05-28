from docstring_parser import rest
import typing
from docstring_parser import numpydoc
from docstring_parser import epydoc
from docstring_parser.common import Docstring
from docstring_parser.common import RenderingStyle
from docstring_parser.common import DocstringStyle
from docstring_parser.attrdoc import add_attribute_docstrings
import inspect
from docstring_parser.common import ParseError
import parser as module_0
from docstring_parser import google
import pytest
def test_example_osx83915():
    assert module_0.parse('This is a test docstring.') != None


def test_example_o7sdybhs():
    obj = type('Test', (), {})
    obj.__doc__ = 'This is a test docstring.'
    assert module_0.parse_from_object(obj).short_description == 'This is a test docstring.'


def test_example_dtc5a43b():
    docstring = module_0.parse('This is a test docstring.\n\nThis is a longer description.')
    assert module_0.compose(docstring) == 'This is a test docstring.\n\nThis is a longer description.'


def test_example_asw7sdms():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.REST)
    assert docstring.style == module_0.DocstringStyle.REST


def test_example_m0gz19y1():
    obj = type('Test', (), {})
    obj.__doc__ = 'This is a test docstring.'
    assert module_0.parse_from_object(obj, style=module_0.DocstringStyle.GOOGLE).short_description == 'This is a test docstring.'


def test_example_iw9dq9n7():
    docstring = module_0.parse('This is a test docstring.\n\nThis is a longer description.', style=module_0.DocstringStyle.NUMPYDOC)
    assert module_0.compose(docstring) != ''


def test_example_p484gnth():
    obj = type('Test', (), {})
    obj.__doc__ = 'This is a test docstring.\n\nThis is a longer description.'
    assert module_0.parse_from_object(obj).long_description == 'This is a longer description.'


def test_example_mluje131():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.EPYDOC)
    assert module_0.compose(docstring, indent='  ') != ''


