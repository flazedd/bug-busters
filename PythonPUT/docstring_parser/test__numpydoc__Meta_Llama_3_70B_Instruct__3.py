import re
from common import DocstringMeta
from textwrap import dedent
from common import DocstringParam
from common import DocstringStyle
from common import RenderingStyle
from common import DocstringDeprecated
import itertools
from common import DocstringRaises
import inspect
from common import DocstringExample
import numpydoc as module_0
import typing
from common import Docstring
from common import DocstringReturns
import pytest
def test_example_454210q5():
    assert module_0.parse('This is a test docstring').style == module_0.DocstringStyle.NUMPYDOC


def test_example_xudeh8ml():
    docstring = '\n    This is a test docstring\n\n    Parameters\n    ----------\n    param1 : int\n        This is the first parameter\n    param2 : str\n        This is the second parameter\n\n    Returns\n    -------\n    int\n        This is the return value\n    '
    parsed_docstring = module_0.parse(docstring)
    assert len(parsed_docstring.params) == 2
    assert parsed_docstring.many_returns[0].type_name == 'int'


def test_example_3lyrgjja():
    docstring = '\n    This is a test docstring\n\n    Examples\n    --------\n    >>> print("Hello, World!")\n    Hello, World!\n    '
    parsed_docstring = module_0.parse(docstring)
    assert len(parsed_docstring.examples) == 1
    assert parsed_docstring.examples[0].snippet == '>>> print("Hello, World!")'


def test_example_trvwg0l7():
    docstring = '\n    This is a test docstring\n\n    Raises\n    ------\n    ValueError\n        This is a value error\n    '
    parsed_docstring = module_0.parse(docstring)
    assert len(parsed_docstring.raises) == 1
    assert parsed_docstring.raises[0].type_name == 'ValueError'


def test_example_yqacsafe():
    docstring = '\n    This is a test docstring\n\n    Warnings\n    --------\n    This is a warning\n    '
    parsed_docstring = module_0.parse(docstring)
    assert len(parsed_docstring.meta) == 1
    assert parsed_docstring.meta[0].args[0] == 'warnings'


def test_example_ssdbwtg3():
    docstring = '\n    This is a test docstring\n\n    Notes\n    -----\n    This is a note\n    '
    parsed_docstring = module_0.parse(docstring)
    assert len(parsed_docstring.meta) == 1
    assert parsed_docstring.meta[0].args[0] == 'notes'


def test_example_xoyj6lwp():
    docstring = '\n    This is a test docstring\n\n    Attributes\n    ----------\n    attr1 : int\n        This is the first attribute\n    attr2 : str\n        This is the second attribute\n    '
    parsed_docstring = module_0.parse(docstring)
    assert len(parsed_docstring.params) == 2
    assert parsed_docstring.params[0].args[0] == 'attribute'
    assert parsed_docstring.params[1].args[0] == 'attribute'


def test_example_umby5d9b():
    docstring = '\n    This is a test docstring\n\n    Yields\n    ------\n    int\n        This is the yield value\n    '
    parsed_docstring = module_0.parse(docstring)
    assert len(parsed_docstring.many_returns) == 1
    assert parsed_docstring.many_returns[0].is_generator
    assert parsed_docstring.many_returns[0].type_name == 'int'


