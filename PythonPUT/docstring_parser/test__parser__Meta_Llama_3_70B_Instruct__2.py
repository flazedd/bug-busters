from docstring_parser.attrdoc import add_attribute_docstrings
from docstring_parser import epydoc
import pytest
from docstring_parser.common import RenderingStyle
from docstring_parser import rest
from docstring_parser.common import ParseError
import parser as module_0
from docstring_parser.common import DocstringStyle
import typing
from docstring_parser import google
import inspect
from docstring_parser.common import Docstring
from docstring_parser import numpydoc
def test_parse_4bfn7rkr():
    text = 'This is a short description.\n\nThis is a long description.'
    docstring = module_0.parse(text)
    assert docstring.short_description == 'This is a short description.'




def test_parse_with_auto_style_nn998k24():
    text = 'This is a short description.\n\nThis is a long description.'
    docstring = module_0.parse(text)
    assert docstring.style != module_0.DocstringStyle.AUTO





def test_parse_8qsau2a7():
    assert isinstance(module_0.parse('This is a test docstring'), module_0.Docstring)





def test_example_mxsm1qpw():
    docstring_text = '\n    This is a sample docstring.\n\n    Parameters:\n    foo (int): The foo parameter.\n    bar (str): The bar parameter.\n\n    Returns:\n    bool: True if successful, False otherwise.\n    '
    parsed_docstring = module_0.parse(docstring_text)
    assert isinstance(parsed_docstring, module_0.Docstring)


def test_example_rg8ds20o():
    obj = type('ExampleClass', (), {'__doc__': 'This is a sample class docstring.'})
    parsed_docstring = module_0.parse_from_object(obj)
    assert isinstance(parsed_docstring, module_0.Docstring)


def test_example_c4gjb7ii():
    docstring_text = '\n    This is a sample docstring.\n\n    Parameters:\n    foo (int): The foo parameter.\n    bar (str): The bar parameter.\n\n    Returns:\n    bool: True if successful, False otherwise.\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert isinstance(rendered_docstring, str)


def test_example_3ouu0kox():
    obj = type('ExampleClass', (), {'__doc__': ''})
    parsed_docstring = module_0.parse_from_object(obj)
    assert isinstance(parsed_docstring, module_0.Docstring)
    assert parsed_docstring.short_description is None
    assert parsed_docstring.long_description is None
    assert not parsed_docstring.meta


def test_example_ryl2zsie():
    docstring_text = '\n    This is a sample docstring.\n\n    Parameters:\n    foo (int): The foo parameter.\n    bar (str): The bar parameter.\n\n    Returns:\n    bool: True if successful, False otherwise.\n    '
    parsed_docstring = module_0.parse(docstring_text, style=module_0.DocstringStyle.REST)
    assert isinstance(parsed_docstring, module_0.Docstring)
    assert parsed_docstring.style == module_0.DocstringStyle.REST


