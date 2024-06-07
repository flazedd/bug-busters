from common import Docstring
from common import EXAMPLES_KEYWORDS
import re
from common import DocstringExample
from common import DocstringParam
from collections import OrderedDict
from common import RenderingStyle
from common import DocstringRaises
from common import PARAM_KEYWORDS
import google as module_0
import inspect
from common import DocstringStyle
import pytest
from collections import namedtuple
from common import ParseError
from common import RAISES_KEYWORDS
from enum import IntEnum
from common import YIELDS_KEYWORDS
from common import DocstringMeta
from common import DocstringReturns
from common import RETURNS_KEYWORDS
import typing
def test_example_s016rn00():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Args:\n        param1 (int): This is the first parameter.\n        param2 (str): This is the second parameter.\n\n    Returns:\n        int: This is the return value.\n\n    Raises:\n        ValueError: This is the error message.\n    ')
    assert isinstance(docstring, module_0.Docstring)





def test_example_zhdmgb7f():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Args:\n        arg1 (int): The first argument.\n        arg2 (str): The second argument.\n\n    Returns:\n        int: The sum of the two arguments.\n\n    Raises:\n        ValueError: If the arguments are invalid.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_8mo5m3ss():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Args:\n        arg1: The first argument.\n        arg2: The second argument.\n\n    Returns:\n        The sum of the two arguments.\n\n    Raises:\n        ValueError\n    ')
    assert any((isinstance(meta, module_0.DocstringParam) for meta in docstring.meta))
    assert any((isinstance(meta, module_0.DocstringReturns) for meta in docstring.meta))
    assert any((isinstance(meta, module_0.DocstringRaises) for meta in docstring.meta))


