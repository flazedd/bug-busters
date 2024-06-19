from docstring_parser.common import DocstringStyle
from docstring_parser.common import RenderingStyle
import parser as module_0
from docstring_parser.attrdoc import add_attribute_docstrings
import inspect
import pytest
from docstring_parser.common import ParseError
import typing
from docstring_parser import epydoc
from docstring_parser import google
from docstring_parser import numpydoc
from docstring_parser.common import Docstring
from docstring_parser import rest
def test_example_yaqe09vr():
    docstring = module_0.parse('This is a test docstring.')
    assert isinstance(docstring, module_0.Docstring)


def test_example_sqyv2dxa():
    obj = type('TestObject', (), {'__doc__': 'This is a test docstring.'})
    docstring = module_0.parse_from_object(obj)
    assert isinstance(docstring, module_0.Docstring)


def test_example_pz5fs7vv():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.GOOGLE)
    assert docstring.style == module_0.DocstringStyle.GOOGLE


def test_example_n3yvq7h7():
    docstring = module_0.parse('This is a test docstring.')
    rendered_docstring = module_0.compose(docstring)
    assert isinstance(rendered_docstring, str)


def test_example_7cckhm36():
    docstring = module_0.parse('This is a test docstring.\n\nParameters:\n    param1: This is a parameter.')
    assert len(docstring.params) == 1


def test_example_hwvhv8hy():
    docstring = module_0.parse('This is a test docstring.\nParameters:\n    param1: This is a parameter.')
    assert len(docstring.params) == 1


def test_example_i82aq3xg():
    docstring = module_0.parse('This is a test docstring.\nRaises:\n    ValueError: This is a raised value.')
    assert len(docstring.raises) == 1


def test_example_24as50x4():
    docstring = module_0.parse('This is a test docstring.')
    assert docstring.short_description == 'This is a test docstring.'


