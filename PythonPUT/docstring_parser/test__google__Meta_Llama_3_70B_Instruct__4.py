from common import Docstring
import google as module_0
from enum import IntEnum
from collections import OrderedDict
from common import DocstringExample
from common import EXAMPLES_KEYWORDS
from common import YIELDS_KEYWORDS
from common import DocstringReturns
from common import RenderingStyle
from common import PARAM_KEYWORDS
import typing
from common import DocstringStyle
from common import DocstringParam
from collections import namedtuple
from common import DocstringMeta
from common import DocstringRaises
import inspect
from common import RAISES_KEYWORDS
import re
import pytest
from common import RETURNS_KEYWORDS
from common import ParseError
def test_example_s016rn00():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Args:\n        param1 (int): This is the first parameter.\n        param2 (str): This is the second parameter.\n\n    Returns:\n        int: This is the return value.\n\n    Raises:\n        ValueError: This is the error message.\n    ')
    assert isinstance(docstring, module_0.Docstring)











def test_example_zhdmgb7f():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Args:\n        arg1 (int): The first argument.\n        arg2 (str): The second argument.\n\n    Returns:\n        int: The sum of the two arguments.\n\n    Raises:\n        ValueError: If the arguments are invalid.\n    ')
    assert isinstance(docstring, module_0.Docstring)








def test_example_k3bqu7q1():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Args:\n        param1: This is the first parameter.\n        param2: This is the second parameter.\n\n    Returns:\n        This is the return value.\n\n    Raises:\n        ValueError: This is an error.\n    ')
    assert isinstance(docstring, module_0.Docstring)





def test_example_3ogvfpbr():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Yields:\n        This is the yield value.\n\n    Raises:\n        ValueError: This is an error.\n    ')
    assert any((isinstance(meta, module_0.DocstringReturns) and meta.is_generator for meta in docstring.meta))





def test_example_317ufoy7():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Args:\n        param1 (int): This is the first parameter.\n        param2 (str): This is the second parameter.\n\n    Returns:\n        str: This is the return value.\n    ')
    assert any((isinstance(meta, module_0.DocstringParam) and meta.arg_name == 'param1' for meta in docstring.meta))





def test_example_i61jiovx():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Attributes:\n        attr1: This is the first attribute.\n        attr2: This is the second attribute.\n\n    Example:\n        >>> foo()\n        bar\n    ')
    assert any((isinstance(meta, module_0.DocstringExample) for meta in docstring.meta))





def test_example_rdcann6v():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        This is a long description.\n\n        Args:\n            arg1: This is arg1 description.\n            arg2: This is arg2 description.\n\n        Returns:\n            This is return description.\n\n        Raises:\n            ValueError: This is ValueError description.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_6wl3rkgd():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        This is a long description.\n\n        Examples:\n            >>> 1 + 1\n            2\n\n        Attributes:\n            attr1: This is attr1 description.\n            attr2: This is attr2 description.\n\n        Yields:\n            This is yield description.\n    ')
    assert len(docstring.meta) == 4


