from common import DocstringExample
from common import YIELDS_KEYWORDS
from common import DocstringParam
import google as module_0
import pytest
from common import DocstringStyle
from common import EXAMPLES_KEYWORDS
from collections import namedtuple
from enum import IntEnum
from common import PARAM_KEYWORDS
from common import RenderingStyle
import inspect
from common import DocstringMeta
from common import Docstring
from collections import OrderedDict
import re
from common import ParseError
from common import DocstringRaises
from common import DocstringReturns
import typing
from common import RETURNS_KEYWORDS
from common import RAISES_KEYWORDS
def test_example_3oj48ukj():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Args:\n            arg1 (int): The first argument.\n            arg2 (str): The second argument.\n\n        Returns:\n            int: The result of the function.\n\n        Raises:\n            ValueError: If the input is invalid.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_irengavg():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Yields:\n            int: The result of the function.\n    ')
    assert isinstance(docstring.many_returns[0], module_0.DocstringReturns)


def test_example_dp9zcwop():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Args:\n            arg1 (int): The first argument.\n            arg2 (str): The second argument.\n\n        Raises:\n            ValueError: If the input is invalid.\n            TypeError: If the input type is incorrect.\n    ')
    assert len([p for p in docstring.meta if isinstance(p, module_0.DocstringRaises)]) == 2


def test_example_8efnvy7j():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Attributes:\n            attr1 (int): The first attribute.\n            attr2 (str): The second attribute.\n            attr3 (bool): The third attribute.\n    ')
    assert len([p for p in docstring.meta if isinstance(p, module_0.DocstringParam)]) == 3


def test_example_ruauv6ir():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Args:\n            arg1: The first argument.\n            arg2: The second argument.\n\n        Returns:\n            int: The result of the function.\n    ')
    assert len(docstring.params) == 2


def test_example_jpljwlwj():
    parser = module_0.GoogleParser()
    docstring = parser.parse("\n        This is a test docstring.\n\n        Examples:\n            >>> func(1, 2)\n            3\n            >>> func('a', 'b')\n            'ab'\n    ")
    assert isinstance(docstring.meta[0], module_0.DocstringExample)


def test_example_fcq4b0wy():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Args:\n            arg1 (int): The first argument.\n            arg2 (str): The second argument.\n\n        Returns:\n            int: The result of the function.\n\n        Raises:\n            ValueError: If the input is invalid.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert 'Args:' in rendered_docstring


def test_example_2nhhwbyi():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Attributes:\n            attr1: The first attribute.\n            attr2: The second attribute.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert 'Attributes:' in rendered_docstring


