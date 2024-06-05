from common import ParseError
import pytest
from common import DocstringReturns
from common import DocstringMeta
import re
import inspect
import typing
from common import Docstring
import epydoc as module_0
from common import DocstringParam
from common import RenderingStyle
from common import DocstringRaises
from common import DocstringStyle
def test_example_p3ubal1e():
    text = '\n    This is a sample docstring.\n\n    :param foo: This is a parameter.\n    :type foo: int\n    :param bar: This is another parameter.\n    :type bar: str\n    :return: This is the return value.\n    :rtype: int\n    :raise ValueError: This is an error.\n    '
    docstring = module_0.parse(text)
    assert isinstance(docstring, module_0.Docstring)





def test_example_gcblguxl():
    text = '\n    This is a sample docstring.\n\n    :param foo: This is a parameter.\n    :type foo: int\n    :return: This is the return value.\n    :rtype: int\n    '
    docstring = module_0.parse(text)
    assert docstring.short_description == 'This is a sample docstring.'





def test_example_iengywnd():
    text = '\n    This is a sample docstring.\n\n    :param garply: This is a parameter.\n    :type garply: tuple\n    :return: This is the return value.\n    :rtype: tuple\n    :raise ValueError: This is an error.\n    '
    docstring = module_0.parse(text)
    assert isinstance(docstring, module_0.Docstring)





def test_example_9fi9tfd1():
    text = '\n    This is a sample docstring.\n\n    :param waldo: This is a parameter.\n    :type waldo: set\n    :return: This is the return value.\n    :rtype: set\n    :raise TypeError: This is an error.\n    '
    docstring = module_0.parse(text)
    assert docstring.style == module_0.DocstringStyle.EPYDOC





def test_example_jtknxa7g():
    text = '\n    This is a sample docstring.\n\n    :param foo: This is a parameter.\n    :type foo: int\n    :param bar: This is another parameter.\n    :type bar: str\n    :return: This is the return value.\n    :rtype: int\n    :raise ValueError: This is an error.\n    '
    docstring = module_0.parse(text)
    assert isinstance(docstring, module_0.Docstring)


def test_example_3vcavrpq():
    text = '\n    This is a sample docstring.\n    '
    docstring = module_0.parse(text)
    assert docstring.short_description == 'This is a sample docstring.'


def test_example_qzumfcea():
    text = '\n    This is a sample docstring.\n\n    This is a long description.\n    '
    docstring = module_0.parse(text)
    assert docstring.long_description == 'This is a long description.'


def test_example_twyqyzjk():
    text = '\n    This is a sample docstring.\n\n    :param foo: This is a parameter.\n    :type foo: int\n    '
    docstring = module_0.parse(text)
    composed = module_0.compose(docstring)
    assert ':param foo:' in composed


