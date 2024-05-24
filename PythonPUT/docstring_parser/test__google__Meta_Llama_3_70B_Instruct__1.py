from common import EXAMPLES_KEYWORDS
from common import ParseError
import typing
from common import DocstringExample
from common import DocstringMeta
import re
from common import DocstringStyle
from common import DocstringRaises
import pytest
from common import YIELDS_KEYWORDS
from collections import OrderedDict
from common import DocstringReturns
from common import RETURNS_KEYWORDS
from enum import IntEnum
import inspect
from common import PARAM_KEYWORDS
from collections import namedtuple
from common import Docstring
from common import DocstringParam
from common import RenderingStyle
import google as module_0
from common import RAISES_KEYWORDS
def test_example_ypab10gh():
    docstring = module_0.parse('\n        This is a short description.\n\n        This is a long description.\n\n        Args:\n            foo (int): The foo argument.\n            bar (str): The bar argument.\n\n        Returns:\n            int: The result.\n\n        Raises:\n            ValueError: If foo is invalid.\n    ')
    assert len(docstring.meta) == 4


def test_example_k5it3cvm():
    docstring = module_0.parse('\n        This is a short description.\n\n        Args:\n            foo (int): The foo argument.\n\n        Returns:\n            int: The result.\n\n        Yields:\n            int: The yielded result.\n\n        Raises:\n            ValueError: If foo is invalid.\n    ')
    assert any((meta.args[0] == 'yields' for meta in docstring.meta))


def test_example_ba02odsy():
    docstring = module_0.parse('\n        This is a short description.\n\n        Args:\n            foo (int, optional): The foo argument. Defaults to 1.\n\n        Returns:\n            int: The result.\n    ')
    assert any((meta.default == '1' for meta in docstring.meta))


def test_example_8182ta94():
    docstring = module_0.parse('\n        This is a short description.\n\n        Examples:\n            >>> foo = 1\n            >>> bar = 2\n    ')
    assert any((isinstance(meta, module_0.DocstringExample) for meta in docstring.meta))


def test_example_t0eeyhst():
    docstring = module_0.parse('\n        This is a short description.\n\n        Attributes:\n            foo (int): The foo attribute.\n            bar (str): The bar attribute.\n    ')
    assert any((meta.args[0] == 'attribute' for meta in docstring.meta))


def test_example_52uawh5p():
    docstring = module_0.parse('\n        This is a short description.\n\n        Args:\n            foo (int): The foo argument.\n            bar (str): The bar argument.\n\n        Returns:\n            int: The result.\n    ')
    rendered_docstring = module_0.compose(docstring, module_0.RenderingStyle.COMPACT)
    assert 'Args:' in rendered_docstring


def test_example_hv4ij1b4():
    docstring = module_0.parse('\n        This is a short description.\n\n        Args:\n            foo: The foo argument.\n\n        Returns:\n            int: The result.\n    ')
    assert any((not meta.type_name for meta in docstring.meta))


def test_example_5nx8l8ic():
    docstring = module_0.parse('\n        This is a short description.\n\n        Raises:\n            ValueError: If foo is invalid.\n            TypeError: If bar is invalid.\n    ')
    assert len([meta for meta in docstring.meta if isinstance(meta, module_0.DocstringRaises)]) == 2


