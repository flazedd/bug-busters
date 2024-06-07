import pytest
import typing
from docstring_parser import rest
import inspect
from docstring_parser.attrdoc import add_attribute_docstrings
from docstring_parser.common import ParseError
from docstring_parser.common import DocstringStyle
from docstring_parser import epydoc
from docstring_parser import google
from docstring_parser import numpydoc
from docstring_parser.common import RenderingStyle
from docstring_parser.common import Docstring
import parser as module_0
def test_example_gdy2rmkl():
    assert module_0.parse('This is a test docstring.') != None


def test_example_4upfg7xk():
    assert module_0.compose(module_0.parse('This is a test docstring.')) != ''


def test_example_9npjue5y():
    obj = type('TestObject', (), {})
    obj.__doc__ = 'This is a test docstring.'
    assert module_0.parse_from_object(obj) != None


def test_example_yya86a2g():
    obj = type('TestClass', (), {})
    obj.__doc__ = 'This is a test class docstring.'
    obj.test_attribute = 'This is a test attribute docstring.'
    assert module_0.parse_from_object(obj).short_description != ''


def test_example_329ubnhr():
    obj = type('TestClass', (), {})
    obj.__doc__ = 'This is a test class docstring.\n\nThis is a longer description.'
    assert module_0.parse(obj.__doc__).long_description != ''


def test_example_biko35zh():
    obj = type('TestClass', (), {})
    obj.__doc__ = 'This is a test class docstring.\n:param test_param: This is a test parameter.'
    parsed_docstring = module_0.parse(obj.__doc__)
    assert any((arg.description == 'This is a test parameter.' for arg in parsed_docstring.meta))


def test_example_gwjt8lwg():
    obj = type('TestClass', (), {})
    obj.__doc__ = 'This is a test class docstring.\n:return: This is a test return value.'
    parsed_docstring = module_0.parse(obj.__doc__)
    assert parsed_docstring.returns.description == 'This is a test return value.'


def test_example_85tu11r6():
    obj = type('TestClass', (), {})
    obj.__doc__ = 'This is a test class docstring.\n:raises Exception: This is a test exception.'
    parsed_docstring = module_0.parse(obj.__doc__)
    assert parsed_docstring.raises[0].description == 'This is a test exception.'


