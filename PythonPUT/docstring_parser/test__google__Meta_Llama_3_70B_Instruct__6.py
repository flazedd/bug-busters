from collections import namedtuple
from common import DocstringExample
from common import Docstring
from common import EXAMPLES_KEYWORDS
from common import RAISES_KEYWORDS
import pytest
from common import DocstringParam
import typing
import inspect
from enum import IntEnum
import google as module_0
from common import PARAM_KEYWORDS
from common import RETURNS_KEYWORDS
from common import DocstringReturns
from common import ParseError
from common import DocstringMeta
from common import DocstringStyle
from common import YIELDS_KEYWORDS
from collections import OrderedDict
from common import DocstringRaises
import re
from common import RenderingStyle
def test_example_c86kfw47():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Args:\n            param1: This is the first parameter.\n            param2: This is the second parameter.\n\n        Returns:\n            This is the return value.\n\n        Raises:\n            ValueError: This is a value error.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_a7uts5xp():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Attributes:\n            attr1: This is the first attribute.\n            attr2: This is the second attribute.\n\n        Examples:\n            This is an example.\n    ')
    assert any((isinstance(meta, module_0.DocstringParam) and meta.args[0] == 'attribute' for meta in docstring.meta))


def test_example_bk8wo5jv():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Args:\n            param1: This is the first parameter.\n            param2: This is the second parameter.\n\n        Returns:\n            This is the return value.\n\n        Raises:\n            ValueError: This is a value error.\n    ')
    rendered_docstring = module_0.compose(docstring, module_0.RenderingStyle.COMPACT)
    assert 'Args:' in rendered_docstring
    assert 'Returns:' in rendered_docstring
    assert 'Raises:' in rendered_docstring


def test_example_u9ar25ty():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Parameters:\n            param1 (int): This is the first parameter.\n            param2 (str): This is the second parameter.\n\n        Yields:\n            This is the yield value.\n\n        Exceptions:\n            TypeError: This is a type error.\n    ')
    assert any((isinstance(meta, module_0.DocstringReturns) and meta.is_generator for meta in docstring.meta))


def test_example_7351eopj():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Args:\n            param1: This is the first parameter.\n            param2 (str, optional): This is the second parameter, defaults to "hello".\n\n        Returns:\n            This is the return value.\n\n        Raises:\n            ValueError: This is a value error.\n    ')
    assert any((isinstance(meta, module_0.DocstringParam) and meta.is_optional for meta in docstring.meta))


def test_example_zskd0b3w():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Attributes:\n            attr1: This is the first attribute.\n            attr2: This is the second attribute.\n\n        Examples:\n            >>> This is an example\n            >>> of a multiline example\n    ')
    assert any((isinstance(meta, module_0.DocstringExample) for meta in docstring.meta))


def test_example_0tpfpgo2():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Args:\n            param1: This is the first parameter.\n            param2: This is the second parameter.\n\n        Returns:\n            This is the return value.\n\n        Raises:\n            ValueError: This is a value error.\n    ')
    rendered_docstring = module_0.compose(docstring, module_0.RenderingStyle.EXPANDED)
    assert '\n    ' in rendered_docstring


def test_example_2s73bvzw():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a test docstring.\n\n        Parameters:\n            param1 (int): This is the first parameter.\n            param2 (str): This is the second parameter.\n\n        Returns:\n            This is the return value.\n\n        Raises:\n            ValueError: This is a value error.\n    ')
    assert docstring.short_description == 'This is a test docstring.'


