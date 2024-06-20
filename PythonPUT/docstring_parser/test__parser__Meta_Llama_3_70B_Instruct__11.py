import pytest
from docstring_parser import numpydoc
import parser as module_0
import typing
from docstring_parser.common import RenderingStyle
from docstring_parser.common import ParseError
from docstring_parser import google
from docstring_parser.attrdoc import add_attribute_docstrings
from docstring_parser.common import DocstringStyle
from docstring_parser import epydoc
from docstring_parser import rest
from docstring_parser.common import Docstring
import inspect
def test_example_ldlqs08b():
    text = 'This is a sample docstring'
    docstring = module_0.parse(text)
    assert isinstance(docstring, module_0.Docstring)


def test_example_h0yfak1n():
    obj = type('ExampleClass', (), {'__doc__': 'This is a sample docstring'})
    docstring = module_0.parse_from_object(obj)
    assert isinstance(docstring, module_0.Docstring)


def test_example_qxhyy5q9():
    text = 'This is a sample docstring'
    docstring = module_0.parse(text)
    rendered_docstring = module_0.compose(docstring)
    assert isinstance(rendered_docstring, str)


def test_example_qf4pntbt():
    text = 'This is a sample docstring'
    docstring = module_0.parse(text, style=module_0.DocstringStyle.REST)
    assert docstring.style == module_0.DocstringStyle.REST


def test_example_pdj8us9u():
    text = 'This is a sample docstring'
    docstring = module_0.parse(text, style=module_0.DocstringStyle.GOOGLE)
    assert docstring.style == module_0.DocstringStyle.GOOGLE


def test_example_e6znby1e():
    obj = type('ExampleClass', (), {'__doc__': 'This is a sample docstring'})
    docstring = module_0.parse_from_object(obj, style=module_0.DocstringStyle.NUMPYDOC)
    assert docstring.style == module_0.DocstringStyle.NUMPYDOC


def test_example_eh8sob91():
    text = 'This is a sample docstring'
    docstring = module_0.parse(text)
    rendered_docstring = module_0.compose(docstring, indent='  ')
    assert isinstance(rendered_docstring, str)


def test_example_01udyns2():
    text = 'This is a sample docstring'
    docstring = module_0.parse(text)
    assert isinstance(docstring, module_0.Docstring)


