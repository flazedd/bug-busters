from common import DocstringReturns
import inspect
from common import DocstringMeta
from textwrap import dedent
import itertools
from common import DocstringRaises
from common import RenderingStyle
from common import Docstring
from common import DocstringExample
from common import DocstringParam
from common import DocstringDeprecated
import numpydoc as module_0
from common import DocstringStyle
import pytest
import typing
import re
def test_example_tyl14rcl():
    docstring = '\n    This is a test function.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    str: A message.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring.startswith('This is a test function.')


def test_example_qx4wmftu():
    docstring = '\n    This is a test function.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument, which is optional.\n\n    Returns:\n    str: A message.\n\n    Yields:\n    int: A number.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Yields' in rendered_docstring


def test_example_tpnjid6g():
    docstring = "\n    This is a test function.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    str: A message.\n\n    Examples:\n    >>> test_function(1, 'hello')\n    'hello 1'\n    >>> test_function(2, 'world')\n    'world 2'\n    "
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Examples:' in rendered_docstring


def test_example_efh6bc8n():
    docstring = '\n    This is a test function.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    str: A message.\n\n    Warns:\n    UserWarning: If arg1 is not a positive integer.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Warns:' in rendered_docstring


def test_example_m2fjbkoc():
    docstring = '\n    This is a test function.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument, which has a default value.\n\n    Returns:\n    str: A message.\n\n    Notes:\n    This function does something interesting.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Notes:' in rendered_docstring


def test_example_8c1t5otx():
    docstring = '\n    This is a test function.\n\n    Attributes:\n    attr1 (int): The first attribute.\n    attr2 (str): The second attribute.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Attributes:' in rendered_docstring


def test_example_47fxt5kk():
    docstring = '\n    This is a test function.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    See Also:\n    another_function\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'See Also:' in rendered_docstring


def test_example_smol61t0():
    docstring = "\n    This is a test function.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument, default is 'hello'.\n\n    Returns:\n    str: A message.\n    "
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert ", default is 'hello'" in rendered_docstring


