import inspect
from docstring_parser import rest
from docstring_parser.common import Docstring
from docstring_parser.common import DocstringStyle
from docstring_parser.common import RenderingStyle
import parser as module_0
import pytest
import typing
from docstring_parser import epydoc
from docstring_parser.attrdoc import add_attribute_docstrings
from docstring_parser import google
from docstring_parser import numpydoc
from docstring_parser.common import ParseError
def test_example_5pytkn7k():
    docstring = module_0.parse('This is a test docstring.')
    assert isinstance(docstring, module_0.Docstring)


def test_example_3exjcc8e():
    obj = type('Test', (), {'__doc__': 'This is a test docstring.'})
    docstring = module_0.parse_from_object(obj)
    assert isinstance(docstring, module_0.Docstring)


def test_example_j8moc9mx():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.GOOGLE)
    assert docstring.style == module_0.DocstringStyle.GOOGLE


def test_example_uezwuepp():
    docstring = module_0.parse('This is a test docstring.')
    rendered_docstring = module_0.compose(docstring)
    assert isinstance(rendered_docstring, str)


def test_example_0m9wqcui():
    docstring = module_0.parse('This is a test docstring.\n\nParameters:\n    param1: This is a parameter.')
    assert len(docstring.params) == 1


def test_example_aui1vr1l():
    docstring = module_0.parse('This is a test docstring.\n\nReturns:\n    result: This is a return value.')
    assert docstring.returns.description == 'This is a return value.'


def test_example_hk2nge6c():
    docstring = module_0.parse('This is a test docstring.\n\nRaises:\n    ValueError: This is a raised exception.')
    assert len(docstring.raises) == 1


def test_example_usg8oifm():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.REST)
    assert docstring.style == module_0.DocstringStyle.REST


