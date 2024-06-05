import pytest
from docstring_parser import epydoc
import inspect
from docstring_parser.attrdoc import add_attribute_docstrings
from docstring_parser.common import RenderingStyle
from docstring_parser import rest
import parser as module_0
import typing
from docstring_parser import google
from docstring_parser.common import Docstring
from docstring_parser import numpydoc
from docstring_parser.common import DocstringStyle
from docstring_parser.common import ParseError
def test_example_i39qpzrz():
    assert module_0.parse('This is a docstring', style=module_0.DocstringStyle.REST).short_description == 'This is a docstring'


def test_example_sncazfun():
    obj = type('ExampleClass', (), {})
    obj.__doc__ = 'This is a class docstring'
    assert module_0.parse_from_object(obj).short_description == 'This is a class docstring'


def test_example_26bz6cem():
    text = 'This is a docstring.\n\nThis is a longer description.'
    assert module_0.parse(text, style=module_0.DocstringStyle.REST).long_description == 'This is a longer description.'


def test_example_rzabyrtw():
    docstring = module_0.parse('This is a docstring.', style=module_0.DocstringStyle.REST)
    assert module_0.compose(docstring) == 'This is a docstring.'


def test_example_nm6r666v():
    text = 'This is a docstring.\n\n:param param1: This is a parameter.\n:param param2: This is another parameter.'
    assert len(module_0.parse(text, style=module_0.DocstringStyle.REST).meta) == 2


def test_example_u3ksdhw7():
    obj = type('ExampleClass', (), {})
    obj.__doc__ = 'This is a class docstring.\n\n:param example_param: This is a parameter.\n:returns: This is a return value.'
    assert module_0.parse_from_object(obj).returns.description == 'This is a return value.'


def test_example_m7zu9h9p():
    text = 'This is a docstring.\n\n:raises ValueError: This is an error.'
    assert module_0.parse(text, style=module_0.DocstringStyle.REST).raises[0].description == 'This is an error.'


def test_example_0juebhr2():
    docstring = module_0.parse('This is a docstring.', style=module_0.DocstringStyle.REST)
    assert module_0.compose(docstring) == 'This is a docstring.'


