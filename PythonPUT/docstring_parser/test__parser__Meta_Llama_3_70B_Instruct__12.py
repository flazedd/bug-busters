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
def test_example_ym86bm5a():
    docstring = module_0.parse('This is a test docstring.')
    assert isinstance(docstring, module_0.Docstring)


def test_example_yz5bd66n():
    obj = type('TestClass', (), {})
    obj.__doc__ = 'This is a test docstring.'
    docstring = module_0.parse_from_object(obj)
    assert isinstance(docstring, module_0.Docstring)


def test_example_8o5svdp3():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.REST)
    rendered_docstring = module_0.compose(docstring, rendering_style=module_0.RenderingStyle.COMPACT)
    assert isinstance(rendered_docstring, str)


def test_example_pxfjn00g():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.GOOGLE)
    assert docstring.style == module_0.DocstringStyle.GOOGLE


def test_example_v095ckro():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.NUMPYDOC)
    assert docstring.style == module_0.DocstringStyle.NUMPYDOC


def test_example_j5ehsin8():
    obj = type('TestClass', (), {})
    obj.__doc__ = 'This is a test docstring.'
    setattr(obj, 'attr', 'This is an attribute docstring.')
    docstring = module_0.parse_from_object(obj, style=module_0.DocstringStyle.EPYDOC)
    assert isinstance(docstring, module_0.Docstring)


def test_example_o0e29t88():
    docstring = module_0.parse('This is a test docstring.', style=module_0.DocstringStyle.AUTO)
    assert isinstance(docstring, module_0.Docstring)


def test_example_meu4a8s6():
    docstring = module_0.parse('This is a test docstring.\n\nReturns:\n    None', style=module_0.DocstringStyle.GOOGLE)
    assert docstring.returns.description == 'None'


