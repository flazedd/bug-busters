import typing
from common import DocstringParam
from textwrap import dedent
from common import RenderingStyle
import re
from common import DocstringExample
import itertools
from common import DocstringMeta
from common import DocstringStyle
import inspect
import pytest
from common import DocstringReturns
from common import Docstring
from common import DocstringRaises
from common import DocstringDeprecated
import numpydoc as module_0
def test_example_6jj493zr():
    text = 'This is a test docstring.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    str: A message.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    '
    parser = module_0.NumpydocParser()
    docstring = parser.parse(text)
    assert isinstance(docstring, module_0.Docstring)





def test_example_rf7xzijb():
    docstring = module_0.parse('This is a short description.\n\nThis is a long description.')
    assert isinstance(docstring, module_0.Docstring)


def test_example_dzosyuar():
    docstring = module_0.parse('.. deprecated:: 1.2.3\nThis is a deprecated function.')
    assert isinstance(docstring.deprecation, module_0.DocstringDeprecated)


def test_example_q65ps8bc():
    docstring = module_0.parse('This is a short description.\n\nParameters\n----------\nparam : int\n    This is a parameter.')
    assert len(docstring.params) == 1


def test_example_0s72o3q1():
    docstring = module_0.parse('This is a short description.\n\nReturns\n-------\nint\n    This is a return value.')
    assert isinstance(docstring.returns, module_0.DocstringReturns)


def test_example_ekh6tozh():
    docstring = module_0.parse('This is a short description.\n\nRaises\n------\nValueError\n    This is an error.')
    assert isinstance(docstring.raises[0], module_0.DocstringRaises)


def test_example_oyjeawcg():
    docstring = module_0.parse('This is a short description.\n\nParameters\n----------\nparam1 : int\n    This is the first parameter.\nparam2 : str\n    This is the second parameter.')
    assert len(docstring.params) == 2


def test_example_luw8vo9q():
    docstring = module_0.parse('This is a short description.\n\nYields\n------\nint\n    This is a yield value.')
    assert isinstance(docstring.returns, module_0.DocstringReturns)


