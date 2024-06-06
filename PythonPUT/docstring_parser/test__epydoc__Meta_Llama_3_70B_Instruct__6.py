from common import DocstringReturns
from common import ParseError
from common import Docstring
from common import DocstringMeta
import pytest
import typing
from common import DocstringParam
from common import DocstringStyle
import inspect
from common import DocstringRaises
import epydoc as module_0
import re
from common import RenderingStyle
def test_example_2jb82xch():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is the description of arg1\n    @type arg1: int\n    @param arg2: This is the description of arg2\n    @type arg2: str\n    @return: This is the return description\n    @rtype: int\n    @raise ValueError: This is the error description\n    '
    docstring = module_0.parse(text)
    assert isinstance(docstring, module_0.Docstring)


def test_example_8p7da7gf():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is the description of arg1\n    @type arg1: int?\n    @param arg2: This is the description of arg2\n    @type arg2: str\n    @return: This is the return description\n    @rtype: int\n    @raise ValueError: This is the error description\n    '
    docstring = module_0.parse(text)
    rendered = module_0.compose(docstring)
    assert 'int?' in rendered


def test_example_j7xqiem3():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is the description of arg1\n    @type arg1: int\n    @param arg2: This is the description of arg2\n    @type arg2: str\n    @return: This is the return description\n    @rtype: int\n    @raise ValueError: This is the error description\n    @meta meta_key: This is the meta description\n    '
    docstring = module_0.parse(text)
    rendered = module_0.compose(docstring)
    assert '@meta meta_key:' in rendered


def test_example_u2onj21i():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is the description of arg1\n    @type arg1: int\n    @param arg2: This is the description of arg2\n    @type arg2: str\n    @return: This is the return description\n    @rtype: int\n    @raise ValueError: This is the error description\n    @meta meta_key: This is the meta description\n    @meta another_key: This is another meta description\n    '
    docstring = module_0.parse(text)
    rendered = module_0.compose(docstring)
    assert '@meta meta_key:' in rendered
    assert '@meta another_key:' in rendered


def test_example_dnjb91m9():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is the description of arg1\n    @type arg1: int\n    @param arg2: This is the description of arg2\n    @type arg2: str\n    @return: This is the return description\n    @rtype: int\n    @raise ValueError: This is the error description\n    @param arg3: This is the description of arg3\n    @type arg3: str?\n    '
    docstring = module_0.parse(text)
    rendered = module_0.compose(docstring)
    assert '@param arg3:' in rendered
    assert 'str?' in rendered


def test_example_555o7nh7():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is the description of arg1\n    @type arg1: int\n    @param arg2: This is the description of arg2\n    @type arg2: str\n    @return: This is the return description\n    @rtype: int\n    @raise ValueError: This is the error description\n    @param arg3: This is the description of arg3\n    @type arg3: str\n    @param arg4: This is the description of arg4\n    @type arg4: int?\n    '
    docstring = module_0.parse(text)
    rendered = module_0.compose(docstring)
    assert '@param arg4:' in rendered
    assert 'int?' in rendered


def test_example_5kgnxvc4():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is the description of arg1\n    @type arg1: int\n    @param arg2: This is the description of arg2\n    @type arg2: str\n    @return: This is the return description\n    @rtype: int\n    @raise ValueError: This is the error description\n    @meta meta_key: This is the meta description\n    @meta another_key: This is another meta description\n    @meta yet_another_key: This is yet another meta description\n    '
    docstring = module_0.parse(text)
    rendered = module_0.compose(docstring)
    assert '@meta meta_key:' in rendered
    assert '@meta another_key:' in rendered
    assert '@meta yet_another_key:' in rendered


def test_example_rvrvuop7():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is the description of arg1\n    @type arg1: int\n    @param arg2: This is the description of arg2\n    @type arg2: str\n    @return: This is the return description\n    @rtype: int\n    @raise ValueError: This is the error description\n    @note: This is a note\n    '
    docstring = module_0.parse(text)
    rendered = module_0.compose(docstring)
    assert '@note: This is a note' in rendered


