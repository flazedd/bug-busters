import numpydoc as module_0
import typing
from common import DocstringExample
from common import DocstringMeta
import re
from common import DocstringStyle
from common import DocstringRaises
import pytest
from textwrap import dedent
import itertools
from common import DocstringReturns
import inspect
from common import Docstring
from common import DocstringParam
from common import RenderingStyle
from common import DocstringDeprecated
def test_example_y9brqiab():
    docstring = module_0.parse('This is a short description.\n\nThis is a long description.')
    assert docstring.short_description == 'This is a short description.'


def test_example_ykhv04jg():
    docstring = module_0.parse('Parameters\n----------\nparam1 : int\n    description of param1')
    assert len(docstring.params) == 1


def test_example_6v3o7ywt():
    docstring = module_0.parse('Returns\n-------\nint\n    description of return value')
    assert docstring.returns.type_name == 'int'


def test_example_k8b93e25():
    docstring = module_0.parse('Raises\n------\nValueError\n    description of error')
    assert len(docstring.raises) == 1


def test_example_6wjddxj2():
    docstring = module_0.parse('This is a short description.\n\nThis is a long description.')
    assert docstring.long_description == 'This is a long description.'


def test_example_0gtb5b4w():
    docstring = module_0.parse('Notes\n-----\nThis is a note.')
    assert len(docstring.meta) == 1


def test_example_qr7600rs():
    docstring = module_0.parse('Parameters\n----------\nparam1 : int, optional\n    description of param1')
    assert docstring.params[0].is_optional


def test_example_51ipufbm():
    docstring = module_0.parse('See Also\n--------\nThis is a reference.')
    assert len(docstring.meta) == 1


