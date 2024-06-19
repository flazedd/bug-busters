from common import EXAMPLES_KEYWORDS
from common import RenderingStyle
from common import DocstringStyle
from common import Docstring
from common import DocstringExample
from collections import namedtuple
import inspect
from common import ParseError
from common import DocstringRaises
from enum import IntEnum
from common import DocstringReturns
from common import RAISES_KEYWORDS
from common import DocstringMeta
from common import RETURNS_KEYWORDS
from common import YIELDS_KEYWORDS
import pytest
import typing
from common import PARAM_KEYWORDS
import google as module_0
from common import DocstringParam
from collections import OrderedDict
import re
def test_example_sfbc56ys():
    docstring = '\n    This is a short description.\n\n    This is a long description.\n\n    Args:\n        param1 (int): This is the first parameter.\n        param2 (str): This is the second parameter.\n\n    Returns:\n        int: This is the return value.\n\n    Raises:\n        ValueError: This is the exception.\n    '
    parsed_docstring = module_0.parse(docstring)
    assert isinstance(parsed_docstring, module_0.Docstring)
    assert parsed_docstring.short_description == 'This is a short description.'
    assert parsed_docstring.long_description == 'This is a long description.'
    assert len(parsed_docstring.meta) == 4
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[1], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(parsed_docstring.meta[3], module_0.DocstringRaises)








def test_example_tzvomk35():
    docstring = '\n    This is a short description.\n\n    Args:\n        param1: This is the first parameter.\n        param2: This is the second parameter.\n\n    Returns:\n        This is the return value.\n\n    Yields:\n        This is the yield value.\n\n    Raises:\n        ValueError: This is the exception.\n    '
    parsed_docstring = module_0.parse(docstring)
    assert isinstance(parsed_docstring, module_0.Docstring)
    assert parsed_docstring.short_description == 'This is a short description.'
    assert parsed_docstring.long_description is None
    assert len(parsed_docstring.meta) == 5
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[1], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(parsed_docstring.meta[3], module_0.DocstringReturns)
    assert isinstance(parsed_docstring.meta[4], module_0.DocstringRaises)








def test_example_ow3t9eyk():
    docstring = '\n    This is a short description.\n\n    Attributes:\n        attr1 (int): This is the first attribute.\n        attr2 (str): This is the second attribute.\n\n    Examples:\n        >>> foo = Foo()\n        >>> foo.bar()\n    '
    parsed_docstring = module_0.parse(docstring)
    assert isinstance(parsed_docstring, module_0.Docstring)
    assert parsed_docstring.short_description == 'This is a short description.'
    assert parsed_docstring.long_description is None
    assert len(parsed_docstring.meta) == 3
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[1], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[2], module_0.DocstringExample)








def test_example_6z6igsur():
    docstring = '\n    This is a short description.\n\n    Args:\n        param1: This is the first parameter.\n        param2 (int, str): This is the second parameter.\n\n    Returns:\n        int, str: This is the return value.\n    '
    parsed_docstring = module_0.parse(docstring)
    assert isinstance(parsed_docstring, module_0.Docstring)
    assert parsed_docstring.short_description == 'This is a short description.'
    assert parsed_docstring.long_description is None
    assert len(parsed_docstring.meta) == 3
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[1], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[2], module_0.DocstringReturns)








def test_example_1g2ip100():
    docstring = '\n    This is a short description.\n\n    Args:\n        param1 (int, optional): This is the first parameter.\n        param2 (str, optional): This is the second parameter.\n\n    Raises:\n        ValueError: This is the exception.\n        TypeError: This is another exception.\n    '
    parsed_docstring = module_0.parse(docstring)
    assert isinstance(parsed_docstring, module_0.Docstring)
    assert parsed_docstring.short_description == 'This is a short description.'
    assert parsed_docstring.long_description is None
    assert len(parsed_docstring.meta) == 4
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[1], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[2], module_0.DocstringRaises)
    assert isinstance(parsed_docstring.meta[3], module_0.DocstringRaises)








def test_example_5ou2tor3():
    docstring = '\n    This is a short description.\n\n    Attributes:\n        attr1: This is the first attribute.\n        attr2: This is the second attribute.\n\n    Returns:\n        This is the return value.\n\n    Yields:\n        This is the yield value.\n    '
    parsed_docstring = module_0.parse(docstring)
    assert isinstance(parsed_docstring, module_0.Docstring)
    assert parsed_docstring.short_description == 'This is a short description.'
    assert parsed_docstring.long_description is None
    assert len(parsed_docstring.meta) == 4
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[1], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(parsed_docstring.meta[3], module_0.DocstringReturns)








def test_example_uhqyxh36():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Args:\n        arg1 (int): This is the first argument.\n        arg2 (str): This is the second argument.\n\n    Returns:\n        int: The sum of arg1 and the length of arg2.\n\n    Raises:\n        ValueError: If arg1 is negative.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_t34ym95f():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Attributes:\n        attr1 (int): This is the first attribute.\n        attr2 (str): This is the second attribute.\n\n    Raises:\n        ValueError: If something bad happens.\n    ')
    assert any((isinstance(meta, module_0.DocstringParam) and meta.arg_name == 'attr1' for meta in docstring.meta))


