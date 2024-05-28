from docstring_parser import rest
from docstring_parser.common import Docstring
import inspect
import typing
from docstring_parser import epydoc
from docstring_parser import google
from docstring_parser import numpydoc
from docstring_parser.common import ParseError
import parser as module_0
from docstring_parser.common import RenderingStyle
import pytest
from docstring_parser.attrdoc import add_attribute_docstrings
from docstring_parser.common import DocstringStyle
def test_parse_7bh5y6l6():
    assert module_0.parse('This is a test docstring.').short_description == 'This is a test docstring.'





def test_compose_4rsjnt3g():
    docstring = module_0.parse('This is a test docstring.')
    assert module_0.compose(docstring) == 'This is a test docstring.'





def test_parse_rest_style_82ellz5u():
    docstring = module_0.parse('This is a test docstring.\n:param arg1: The first argument.', style=module_0.DocstringStyle.REST)
    for param in docstring.meta:
        if param.arg_name == 'arg1':
            assert param.description == 'The first argument.'
            break
    else:
        assert False, "Parameter 'arg1' not found"





def test_compose_pjoqj2wr():
    docstring = module_0.parse('This is a test docstring.\n\nArgs:\n    arg1 (int): The first argument.')
    composed_docstring = module_0.compose(docstring, style=module_0.DocstringStyle.REST)
    assert 'This is a test docstring.' in composed_docstring
    assert 'param int arg1: The first argument.' in composed_docstring





def test_parse_multiple_params_ik02v33n():
    docstring = module_0.parse('This is a test docstring.\n\nArgs:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.')
    params = [meta.arg_name for meta in docstring.meta]
    assert 'arg1' in params
    assert 'arg2' in params





def test_parse_return_value_zxao0e84():
    docstring = module_0.parse('This is a test docstring.\n\nReturns:\n    int: The result.')
    assert docstring.returns
    assert docstring.returns.type_name == 'int'
    assert docstring.returns.description == 'The result.'





def test_example_q3gv8jho():
    docstring = module_0.parse('This is a test docstring.')
    assert isinstance(docstring, module_0.Docstring)


def test_example_l9wpkjey():
    obj = type('ExampleClass', (), {})
    obj.__doc__ = 'This is a test docstring.'
    parsed_docstring = module_0.parse_from_object(obj)
    assert isinstance(parsed_docstring, module_0.Docstring)


