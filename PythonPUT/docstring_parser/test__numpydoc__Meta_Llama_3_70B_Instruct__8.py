from common import RenderingStyle
from common import Docstring
from common import DocstringStyle
from common import DocstringExample
import inspect
from common import DocstringDeprecated
from common import DocstringRaises
from common import DocstringReturns
import numpydoc as module_0
from common import DocstringMeta
import pytest
import typing
from common import DocstringParam
from textwrap import dedent
import re
import itertools
def test_example_3c0qb1se():
    docstring = '\n    This is a test docstring.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    int: The result of the operation.\n\n    Raises:\n    ValueError: If the arguments are invalid.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring.startswith('This is a test docstring.')
    assert 'Parameters:' in rendered_docstring
    assert 'Returns:' in rendered_docstring
    assert 'Raises:' in rendered_docstring


def test_example_cz08vz6k():
    docstring = '\n    This is a test docstring.\n\n    Examples:\n    >>> import numpy as np\n    >>> np.array([1, 2, 3])\n    array([1, 2, 3])\n\n    >>> np.array([4, 5, 6])\n    array([4, 5, 6])\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Examples:' in rendered_docstring
    assert '>>> import numpy as np' in rendered_docstring
    assert 'array([1, 2, 3])' in rendered_docstring
    assert 'array([4, 5, 6])' in rendered_docstring


def test_example_3aatsydq():
    docstring = '\n    This is a test docstring.\n\n    Deprecation:\n   .. deprecated:: 1.2.3\n       This function is deprecated since version 1.2.3.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Deprecation:' in rendered_docstring
    assert '.. deprecated:: 1.2.3' in rendered_docstring
    assert 'This function is deprecated since version 1.2.3.' in rendered_docstring


def test_example_aymp3vx3():
    docstring = '\n    This is a test docstring.\n\n    Attributes:\n    attr1 (int): The first attribute.\n    attr2 (str): The second attribute.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Attributes:' in rendered_docstring
    assert 'attr1 (int): The first attribute.' in rendered_docstring
    assert 'attr2 (str): The second attribute.' in rendered_docstring


def test_example_kj2wj8yr():
    docstring = '\n    This is a test docstring.\n\n    Yields:\n    int: The yielded value.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Yields:' in rendered_docstring
    assert 'int: The yielded value.' in rendered_docstring


def test_example_vdq68mm8():
    docstring = '\n    This is a test docstring.\n\n    Warnings:\n    Warning about something.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Warnings:' in rendered_docstring
    assert 'Warning about something.' in rendered_docstring


def test_example_33h4hnkk():
    docstring = '\n    This is a test docstring.\n\n    Notes:\n    This is a note.\n    It can span multiple lines.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'Notes:' in rendered_docstring
    assert 'This is a note.' in rendered_docstring
    assert 'It can span multiple lines.' in rendered_docstring


def test_example_scnqe1wp():
    docstring = '\n    This is a test docstring.\n\n    See Also:\n    Some other function.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert 'See Also:' in rendered_docstring
    assert 'Some other function.' in rendered_docstring


