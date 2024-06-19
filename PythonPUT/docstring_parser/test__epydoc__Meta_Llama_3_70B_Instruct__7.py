from common import DocstringParam
import pytest
from common import DocstringStyle
import epydoc as module_0
import re
from common import ParseError
from common import DocstringRaises
from common import RenderingStyle
import inspect
import typing
from common import DocstringMeta
from common import DocstringReturns
from common import Docstring
def test_example_ib3jvbwh():
    docstring_text = '\n    This is a test docstring.\n\n    :param foo: This is a parameter.\n    :type foo: int\n    :param bar: This is another parameter.\n    :type bar: str\n    :return: This is the return value.\n    :rtype: bool\n    :raise ValueError: This is an exception.\n    '
    parsed_docstring = module_0.parse(inspect.cleandoc(docstring_text))
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.COMPACT)
    assert rendered_docstring == '\nThis is a test docstring.\n\n:param foo: This is a parameter.\n:type foo: int\n:param bar: This is another parameter.\n:type bar: str\n:return: This is the return value.\n:rtype: bool\n:raise ValueError: This is an exception.\n'.strip()


def test_example_1mdr7b66():
    docstring_text = "\n    This is a test docstring.\n\n    :param foo: This is a parameter with a default value.\n    :type foo: int\n    :param bar: This is another parameter with a default value.\n    :type bar: str = 'default value'\n    :return: This is the return value.\n    :rtype: bool\n    :raise ValueError: This is an exception.\n    "
    parsed_docstring = module_0.parse(inspect.cleandoc(docstring_text))
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.COMPACT)
    assert rendered_docstring == "\nThis is a test docstring.\n\n:param foo: This is a parameter with a default value.\n:type foo: int\n:param bar: This is another parameter with a default value.\n:type bar: str = 'default value'\n:return: This is the return value.\n:rtype: bool\n:raise ValueError: This is an exception.\n".strip()


def test_example_hso25jy5():
    docstring_text = '\n    This is a test docstring.\n\n    :param foo: This is a parameter.\n    :type foo: int\n    :param bar: This is another parameter.\n    :type bar: str\n    :return: This is the return value.\n    :rtype: bool\n    :raises ValueError: This is an exception.\n    :raises TypeError: This is another exception.\n    '
    parsed_docstring = module_0.parse(inspect.cleandoc(docstring_text))
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.COMPACT)
    assert rendered_docstring == '\nThis is a test docstring.\n\n:param foo: This is a parameter.\n:type foo: int\n:param bar: This is another parameter.\n:type bar: str\n:return: This is the return value.\n:rtype: bool\n:raises ValueError: This is an exception.\n:raises TypeError: This is another exception.\n'.strip()


def test_example_wv38avll():
    docstring_text = '\n    This is a test docstring.\n\n    :param foo: This is a parameter.\n    :type foo: int\n    :param bar: This is another parameter.\n    :type bar: str\n    :return: This is the return value.\n    :rtype: bool\n    :note: This is a note.\n    :warning: This is a warning.\n    '
    parsed_docstring = module_0.parse(inspect.cleandoc(docstring_text))
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.COMPACT)
    assert rendered_docstring == '\nThis is a test docstring.\n\n:param foo: This is a parameter.\n:type foo: int\n:param bar: This is another parameter.\n:type bar: str\n:return: This is the return value.\n:rtype: bool\n:note: This is a note.\n:warning: This is a warning.\n'.strip()


def test_example_u2p4g3eg():
    docstring_text = '\n    This is a test docstring.\n\n    :param foo: This is a parameter.\n    :type foo: int\n    :param bar: This is another parameter.\n    :type bar: str\n    :return: This is the return value.\n    :rtype: bool\n    :see: https://example.com for more information.\n    '
    parsed_docstring = module_0.parse(inspect.cleandoc(docstring_text))
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.COMPACT)
    assert rendered_docstring == '\nThis is a test docstring.\n\n:param foo: This is a parameter.\n:type foo: int\n:param bar: This is another parameter.\n:type bar: str\n:return: This is the return value.\n:rtype: bool\n:see: https://example.com for more information.\n'.strip()


def test_example_7bhmir4m():
    docstring_text = '\n    This is a test docstring.\n\n    :param foo: This is a parameter.\n    :type foo: int\n    :param bar: This is another parameter.\n    :type bar: str\n    :return: This is the return value.\n    :rtype: bool\n    :author: John Doe\n    :version: 1.0\n    '
    parsed_docstring = module_0.parse(inspect.cleandoc(docstring_text))
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.COMPACT)
    assert rendered_docstring == '\nThis is a test docstring.\n\n:param foo: This is a parameter.\n:type foo: int\n:param bar: This is another parameter.\n:type bar: str\n:return: This is the return value.\n:rtype: bool\n:author: John Doe\n:version: 1.0\n'.strip()


def test_example_jtte24o2():
    docstring_text = '\n    This is a test docstring.\n\n    :param foo: This is a parameter.\n    :type foo: int\n    :param bar: This is another parameter.\n    :type bar: str\n    :return: This is the return value.\n    :rtype: bool\n    :ivar foo: This is an instance variable.\n    :ivar bar: This is another instance variable.\n    '
    parsed_docstring = module_0.parse(inspect.cleandoc(docstring_text))
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.COMPACT)
    assert rendered_docstring == '\nThis is a test docstring.\n\n:param foo: This is a parameter.\n:type foo: int\n:param bar: This is another parameter.\n:type bar: str\n:return: This is the return value.\n:rtype: bool\n:ivar foo: This is an instance variable.\n:ivar bar: This is another instance variable.\n'.strip()


def test_example_t8ltee0l():
    docstring_text = '\n    This is a test docstring.\n\n    :param foo: This is a parameter.\n    :type foo: int\n    :param bar: This is another parameter.\n    :type bar: str\n    :return: This is the return value.\n    :rtype: bool\n    :cvar foo: This is a class variable.\n    :cvar bar: This is another class variable.\n    '
    parsed_docstring = module_0.parse(inspect.cleandoc(docstring_text))
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.COMPACT)
    assert rendered_docstring == '\nThis is a test docstring.\n\n:param foo: This is a parameter.\n:type foo: int\n:param bar: This is another parameter.\n:type bar: str\n:return: This is the return value.\n:rtype: bool\n:cvar foo: This is a class variable.\n:cvar bar: This is another class variable.\n'.strip()


