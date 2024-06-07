from common import Docstring
from textwrap import dedent
from common import DocstringExample
from common import DocstringDeprecated
from common import DocstringReturns
from common import RenderingStyle
import typing
from common import DocstringStyle
from common import DocstringParam
from common import DocstringMeta
import itertools
import numpydoc as module_0
import inspect
from common import DocstringRaises
import re
import pytest
def test_example_ozk00g74():
    assert 1 == 1


def test_example_mmu8754c():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    int: The sum of arg1 and the length of arg2.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    ')
    assert docstring.short_description == 'This is a test docstring.'


def test_example_u9tb4p7k():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    int: The sum of arg1 and the length of arg2.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    ')
    assert docstring.style == DocstringStyle.NUMPYDOC


def test_example_ja5uxk0m():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    int: The sum of arg1 and the length of arg2.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert 'Parameters:' in rendered_docstring


def test_example_cvu8ouw1():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Attributes:\n    attr1 (int): The first attribute.\n    attr2 (str): The second attribute.\n    ')
    assert len(docstring.attributes) == 2


