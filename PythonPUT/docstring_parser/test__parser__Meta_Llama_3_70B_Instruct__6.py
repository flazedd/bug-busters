from docstring_parser.common import DocstringStyle
from docstring_parser.common import ParseError
from docstring_parser.attrdoc import add_attribute_docstrings
from docstring_parser import epydoc
from docstring_parser.common import Docstring
from docstring_parser.common import RenderingStyle
from docstring_parser import numpydoc
import inspect
import parser as module_0
from docstring_parser import google
import pytest
import typing
from docstring_parser import rest
def test_example_8fuze5sw():
    assert module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.REST).short_description == 'This is a test docstring.'


def test_example_9c9guswv():
    obj = type('TestObject', (), {})
    obj.__doc__ = 'This is a test docstring.'
    assert module_0.parse_from_object(obj).short_description == 'This is a test docstring.'


def test_example_wnovfc36():
    docstring = module_0.parse('This is a test docstring.\n\nThis is a longer description.', style=module_0.DocstringStyle.REST)
    assert module_0.compose(docstring) == 'This is a test docstring.\n\nThis is a longer description.'


def test_example_wjxn70fg():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.GOOGLE)
    assert module_0.compose(docstring, rendering_style=module_0.RenderingStyle.COMPACT) == 'This is a test docstring.'


def test_example_21pyt4y7():
    obj = type('TestObject', (), {})
    obj.__doc__ = 'This is a test docstring.\n\nThis is a longer description.'
    docstring = module_0.parse_from_object(obj)
    assert module_0.compose(docstring) == 'This is a test docstring.\n\nThis is a longer description.'


def test_example_2wohz1ec():
    docstring = module_0.parse('This is a test docstring.\n\n:param foo: foo description', style=module_0.DocstringStyle.REST)
    assert docstring.params[0].arg_name == 'foo'


def test_example_lugc5iqu():
    obj = type('TestObject', (), {})
    obj.__doc__ = 'This is a test docstring.\n\n:param foo: foo description\n:param bar: bar description'
    docstring = module_0.parse_from_object(obj)
    assert len(docstring.params) == 2


def test_example_2zqwkkzk():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.REST)
    assert docstring.short_description == 'This is a test docstring.'


