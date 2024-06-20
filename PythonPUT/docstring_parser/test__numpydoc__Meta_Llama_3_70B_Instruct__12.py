from common import Docstring
import pytest
from common import RenderingStyle
import typing
from common import DocstringStyle
from common import DocstringRaises
from common import DocstringMeta
import re
import itertools
from common import DocstringParam
from common import DocstringExample
from textwrap import dedent
import numpydoc as module_0
from common import DocstringReturns
import inspect
from common import DocstringDeprecated
def test_example_4rpzdrhj():
    docstring = '\n    This is a test docstring.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    int: The result of the function.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring.startswith('This is a test docstring.')


def test_example_a2a35tda():
    docstring = '\n    This is a test docstring.\n\n    Examples:\n    >>> import numpy as np\n    >>> np.array([1, 2, 3])\n    array([1, 2, 3])\n    >>> np.array([1, 2, 3], dtype=int)\n    array([1, 2, 3])\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Examples:' in rendered_docstring


def test_example_84lzowmt():
    docstring = '\n    This is a test docstring.\n\n    Attributes:\n    attr1 (int): The first attribute.\n    attr2 (str): The second attribute.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Attributes:' in rendered_docstring


def test_example_b9mvkbev():
    docstring = '\n    This is a test docstring.\n\n    Yields:\n    int: The yielded value.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Yields:' in rendered_docstring


def test_example_zzx2zne1():
    docstring = '\n    This is a test docstring.\n\n    Deprecation:\n   .. deprecated:: 1.2.3\n       This function is deprecated.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert '.. deprecated:: 1.2.3' in rendered_docstring


def test_example_lyfqc629():
    docstring = "\n    This is a test docstring.\n\n    Parameters:\n    arg1 (int): The first argument. Defaults to 1.\n    arg2 (str): The second argument. Defaults to 'hello'.\n    "
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Defaults to 1' in rendered_docstring
    assert "Defaults to 'hello'" in rendered_docstring


def test_example_rhu7ra2d():
    docstring = '\n    This is a test docstring.\n\n    Warnings:\n    Warning message.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Warnings:' in rendered_docstring
    assert 'Warning message.' in rendered_docstring


def test_example_n5w6842m():
    docstring = '\n    This is a test docstring.\n\n    See Also:\n    Some other function.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'See Also:' in rendered_docstring
    assert 'Some other function.' in rendered_docstring


