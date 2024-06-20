import parser as module_0
from docstring_parser import rest
from docstring_parser import epydoc
from docstring_parser.common import Docstring
from docstring_parser.common import DocstringStyle
import inspect
from docstring_parser import google
from docstring_parser import numpydoc
import typing
from docstring_parser.common import RenderingStyle
from docstring_parser.attrdoc import add_attribute_docstrings
import pytest
from docstring_parser.common import ParseError
def test_example_3et8ujrq():
    docstring_text = 'This is a test docstring.'
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring == 'This is a test docstring.'


def test_example_t39ly4so():

    class MyClass:
        """This is a class docstring."""

        def __init__(self):
            """This is an init docstring."""
            pass

        def my_method(self):
            """This is a method docstring."""
            pass
    parsed_docstring = module_0.parse_from_object(MyClass)
    assert 'This is a class docstring.' in parsed_docstring.short_description


def test_example_iskih8yp():

    class MyClass:
        """This is a class docstring.
        
        This is a longer description.
        """

        def __init__(self):
            """This is an init docstring."""
            pass

        def my_method(self):
            """This is a method docstring."""
            pass
    parsed_docstring = module_0.parse_from_object(MyClass)
    assert 'This is a longer description.' in parsed_docstring.long_description


def test_example_ytzje5bt():
    docstring_text = 'This is a test docstring.\n\nThis is a longer description.'
    parsed_docstring = module_0.parse(docstring_text)
    assert 'This is a longer description.' in parsed_docstring.long_description


def test_example_jw4k8jsm():
    docstring_text = 'This is a test docstring.\n:param param1: This is a parameter.'
    parsed_docstring = module_0.parse(docstring_text)
    assert 'param1' in [param.arg_name for param in parsed_docstring.params]


def test_example_de4j1klw():
    docstring_text = 'This is a test docstring.\n:return: This is a return value.'
    parsed_docstring = module_0.parse(docstring_text)
    assert 'This is a return value.' in parsed_docstring.returns.description


def test_example_0md0lakt():
    docstring_text = 'This is a test docstring.\n:param param1: This is a parameter.\n:type param1: int'
    parsed_docstring = module_0.parse(docstring_text)
    assert 'int' in [param.type_name for param in parsed_docstring.params]


def test_example_uineby8v():
    docstring_text = 'This is a test docstring.\n:return: This is a return value.\n:rtype: str'
    parsed_docstring = module_0.parse(docstring_text)
    assert 'str' == parsed_docstring.returns.type_name


