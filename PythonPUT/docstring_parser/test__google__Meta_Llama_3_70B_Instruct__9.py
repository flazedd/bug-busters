from common import EXAMPLES_KEYWORDS
from collections import OrderedDict
from common import DocstringReturns
import inspect
from common import PARAM_KEYWORDS
from common import RenderingStyle
from common import Docstring
from common import YIELDS_KEYWORDS
from common import DocstringMeta
from common import DocstringExample
from common import DocstringRaises
from common import RETURNS_KEYWORDS
from enum import IntEnum
from common import ParseError
from common import DocstringStyle
from collections import namedtuple
import typing
import re
from common import DocstringParam
from common import RAISES_KEYWORDS
import pytest
import google as module_0
def test_example_ol8rskev():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        This is a long description.\n\n        Args:\n            param1 (int): This is the first parameter.\n            param2 (str): This is the second parameter.\n\n        Returns:\n            int: This is the return value.\n\n        Raises:\n            ValueError: This is the error message.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description.'
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)


def test_example_2qnqoyuo():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        This is a long description.\n\n        Attributes:\n            attr1 (int): This is the first attribute.\n            attr2 (str): This is the second attribute.\n\n        Yields:\n            int: This is the yield value.\n\n        Raises:\n            ValueError: This is the error message.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description.'
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)


def test_example_0m99inkr():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        This is a long description.\n\n        Examples:\n            This is an example.\n\n        Args:\n            param1 (int): This is the first parameter.\n\n        Returns:\n            int: This is the return value.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description.'
    assert len(docstring.meta) == 3
    assert isinstance(docstring.meta[0], module_0.DocstringExample)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)


def test_example_movknenr():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        Args:\n            param1 (int): This is the first parameter.\n            param2 (str): This is the second parameter.\n            param3: This is the third parameter.\n\n        Returns:\n            int: This is the return value.\n\n        Raises:\n            ValueError: This is the error message.\n            TypeError: This is another error message.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description is None
    assert len(docstring.meta) == 6
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringParam)
    assert isinstance(docstring.meta[3], module_0.DocstringReturns)
    assert isinstance(docstring.meta[4], module_0.DocstringRaises)
    assert isinstance(docstring.meta[5], module_0.DocstringRaises)


def test_example_lwgkq5qn():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        Args:\n            param1: This is the first parameter.\n            param2: This is the second parameter.\n\n        Returns:\n            This is the return value.\n\n        Yields:\n            This is the yield value.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description is None
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringReturns)


def test_example_g5j38zfy():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        Args:\n            param1 (int, str): This is the first parameter.\n            param2: This is the second parameter.\n\n        Returns:\n            int, str: This is the return value.\n\n        Raises:\n            ValueError, TypeError: This is the error message.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description is None
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)


def test_example_nbogek0c():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        Attributes:\n            attr1 (int): This is the first attribute.\n            attr2 (str): This is the second attribute.\n\n        Examples:\n            This is an example.\n\n        Yields:\n            int: This is the yield value.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description is None
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringExample)
    assert isinstance(docstring.meta[3], module_0.DocstringReturns)


def test_example_dlx0b3p8():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        Args:\n            param1 (int): This is the first parameter.\n            param2 (str): This is the second parameter.\n\n        Returns:\n            int: This is the return value.\n\n        Raises:\n            ValueError: This is the error message.\n            TypeError: This is another error message.\n\n        Notes:\n            This is a note.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description is None
    assert len(docstring.meta) == 5
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)
    assert isinstance(docstring.meta[4], module_0.DocstringMeta)


