from docstring_parser import epydoc
from docstring_parser import numpydoc
from docstring_parser.common import RenderingStyle
import parser as module_0
from docstring_parser import rest
from docstring_parser.attrdoc import add_attribute_docstrings
import inspect
import typing
from docstring_parser.common import Docstring
from docstring_parser.common import ParseError
import pytest
from docstring_parser import google
from docstring_parser.common import DocstringStyle
def test_example_wf5jcm16():
    text = 'This is a test docstring.'
    style = module_0.DocstringStyle.AUTO
    docstring = module_0.parse(text, style)
    assert isinstance(docstring, module_0.Docstring)


def test_example_53t8fqy8():
    obj = type('ExampleClass', (), {})
    obj.__doc__ = 'This is a test docstring.'
    style = module_0.DocstringStyle.AUTO
    docstring = module_0.parse_from_object(obj, style)
    assert isinstance(docstring, module_0.Docstring)


def test_example_ephh1pgy():
    text = 'This is a test docstring.'
    style = module_0.DocstringStyle.GOOGLE
    docstring = module_0.parse(text, style)
    assert docstring.short_description == 'This is a test docstring.'


def test_example_erqxivkb():
    obj = type('ExampleClass', (), {})
    obj.__doc__ = 'This is a test docstring.\n\nMore information.'
    style = module_0.DocstringStyle.NUMPYDOC
    docstring = module_0.parse_from_object(obj, style)
    assert docstring.long_description == 'More information.'


def test_example_znsuo3d7():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.EPYDOC)
    composed_docstring = module_0.compose(docstring, style=module_0.DocstringStyle.EPYDOC)
    assert composed_docstring == 'This is a test docstring.'


def test_example_hbtlpryb():
    text = 'This is a test docstring.\n\n:return: This is a return value.'
    style = module_0.DocstringStyle.REST
    docstring = module_0.parse(text, style)
    assert docstring.returns.description == 'This is a return value.'


def test_example_w79ykznc():
    text = 'This is a test docstring.\n\nExample:'
    style = module_0.DocstringStyle.GOOGLE
    docstring = module_0.parse(text, style)
    assert len(docstring.examples) == 1


def test_example_h3ca647a():
    text = 'This is a test docstring.\n\n:raises Exception: This is an exception.'
    style = module_0.DocstringStyle.REST
    docstring = module_0.parse(text, style)
    assert len(docstring.raises) == 1


