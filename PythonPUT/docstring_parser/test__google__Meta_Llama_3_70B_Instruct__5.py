from common import DocstringReturns
from collections import namedtuple
import inspect
from common import DocstringMeta
from collections import OrderedDict
from common import DocstringRaises
from common import YIELDS_KEYWORDS
from common import RenderingStyle
from common import Docstring
from common import DocstringExample
import google as module_0
from common import DocstringParam
from common import DocstringStyle
import pytest
from common import ParseError
from common import EXAMPLES_KEYWORDS
from enum import IntEnum
from common import RETURNS_KEYWORDS
import typing
from common import PARAM_KEYWORDS
import re
from common import RAISES_KEYWORDS
def test_example_ib9lsscl():
    text = '\n        This is a test docstring.\n\n        Args:\n            arg1 (int): The first argument.\n            arg2 (str): The second argument.\n\n        Returns:\n            int: The sum of the arguments.\n\n        Raises:\n            ValueError: If the arguments are invalid.\n    '
    parser = module_0.GoogleParser()
    docstring = parser.parse(text)
    assert isinstance(docstring, module_0.Docstring)





def test_example_yrdcgmbx():
    text = "\n        This is a test docstring.\n\n        Examples:\n            >>> func(1, 2)\n            3\n            >>> func('a', 'b')\n            'ab'\n\n        Attributes:\n            attr1 (int): The first attribute.\n            attr2 (str): The second attribute.\n\n        Yields:\n            int: The yielded value.\n    "
    parser = module_0.GoogleParser()
    docstring = parser.parse(text)
    assert isinstance(docstring, module_0.Docstring)





def test_example_3i7yar9j():
    text = '\n        This is a test docstring.\n\n        Parameters:\n            param1 (int): The first parameter.\n            param2 (str): The second parameter.\n\n        Returns:\n            str: The concatenated parameters.\n\n        Except:\n            TypeError: If the parameters are of invalid types.\n    '
    parser = module_0.GoogleParser()
    docstring = parser.parse(text)
    assert isinstance(docstring, module_0.Docstring)





def test_example_x9u8331b():
    text = "\n        This is a test docstring.\n\n        Args:\n            arg1 (int): The first argument.\n            arg2 (str): The second argument.\n\n        Returns:\n            str: The concatenated arguments.\n\n        Raises:\n            TypeError: If the arguments are of invalid types.\n\n        Examples:\n            >>> func(1, 'a')\n            '1a'\n            >>> func('a', 1)\n            'a1'\n    "
    parser = module_0.GoogleParser()
    docstring = parser.parse(text)
    assert isinstance(docstring, module_0.Docstring)
    assert len(docstring.meta) == 5
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)
    assert isinstance(docstring.meta[4], module_0.DocstringExample)





def test_example_obroiy8g():
    text = "\n        This is a test docstring.\n\n        Args:\n            arg1: The first argument.\n            arg2 (str): The second argument.\n\n        Returns:\n            str: The concatenated arguments.\n\n        Raises:\n            TypeError: If the arguments are of invalid types.\n\n        Examples:\n            >>> func(1, 'a')\n            '1a'\n            >>> func('a', 1)\n            'a1'\n    "
    parser = module_0.GoogleParser()
    docstring = parser.parse(text)
    assert isinstance(docstring, module_0.Docstring)
    assert len(docstring.meta) == 5
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)
    assert isinstance(docstring.meta[4], module_0.DocstringExample)





def test_example_smlnn2en():
    text = "\n        This is a test docstring.\n\n        Attributes:\n            attr1 (int): The first attribute.\n            attr2: The second attribute.\n\n        Yields:\n            int: The yielded value.\n\n        Examples:\n            >>> func(1, 2)\n            3\n            >>> func('a', 'b')\n            'ab'\n    "
    parser = module_0.GoogleParser()
    docstring = parser.parse(text)
    assert isinstance(docstring, module_0.Docstring)
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringExample)





def test_example_jmyw1c52():
    text = "\n        This is a test docstring.\n\n        Parameters:\n            param1 (int): The first parameter.\n            param2: The second parameter.\n\n        Returns:\n            str: The concatenated parameters.\n\n        Except:\n            TypeError: If the parameters are of invalid types.\n\n        Examples:\n            >>> func(1, 'a')\n            '1a'\n            >>> func('a', 1)\n            'a1'\n    "
    parser = module_0.GoogleParser()
    docstring = parser.parse(text)
    assert isinstance(docstring, module_0.Docstring)
    assert len(docstring.meta) == 5
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)
    assert isinstance(docstring.meta[4], module_0.DocstringExample)





def test_example_2dbufiyb():
    docstring = module_0.parse('\n        This is a test docstring.\n\n        Args:\n            param1 (int): This is a parameter.\n            param2 (str): This is another parameter.\n\n        Returns:\n            int: This is a return value.\n\n        Raises:\n            ValueError: This is an exception.\n    ')
    assert isinstance(docstring, module_0.Docstring)


