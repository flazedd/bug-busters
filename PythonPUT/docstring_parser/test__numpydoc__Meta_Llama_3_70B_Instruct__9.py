from common import DocstringReturns
import inspect
from common import RenderingStyle
from common import Docstring
from common import DocstringMeta
from common import DocstringExample
from common import DocstringRaises
import itertools
from common import DocstringDeprecated
from common import DocstringStyle
import typing
import numpydoc as module_0
import re
from common import DocstringParam
import pytest
from textwrap import dedent
def test_example_zjbkua49():
    import numpydoc as module_0
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Parameters\n    ----------\n    param1 : int\n        This is a test parameter.\n    param2 : str\n        This is another test parameter.\n\n    Returns\n    -------\n    int\n        This is a test return value.\n\n    Raises\n    ------\n    ValueError\n        This is a test error.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_y6ire1cr():
    import numpydoc as module_0
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Examples\n    --------\n    >>> import numpy.matlib\n    >>> np.matlib.empty((2, 2))    # filled with random data\n    matrix([[  6.76425276e-320,   9.79033856e-307], # random\n            [  7.39337286e-309,   3.22135945e-309]])\n    >>> np.matlib.empty((2, 2), dtype=int)\n    matrix([[ 6600475,        0], # random\n            [ 6586976, 22740995]])\n    ')
    assert len(docstring.examples) == 2


def test_example_zw3axnjz():
    import numpydoc as module_0
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Deprecation\n    ----------\n   .. deprecated:: 1.2.3\n       This is a test deprecation warning.\n    ')
    assert docstring.deprecation is not None


def test_example_ob7lhdet():
    import numpydoc as module_0
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Attributes\n    ----------\n    attr1 : int\n        This is a test attribute.\n    attr2 : str\n        This is another test attribute.\n    ')
    assert len(docstring.params) == 2


def test_example_sp4atsm9():
    import numpydoc as module_0
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Notes\n    -----\n    This is a test note.\n    ')
    assert docstring.meta[0].description == 'This is a test note.'


def test_example_ns4rwdn3():
    import numpydoc as module_0
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Returns\n    -------\n    int\n        This is a test return value.\n    ')
    assert docstring.returns.type_name == 'int'


def test_example_qzz8bzth():
    import numpydoc as module_0
    docstring = module_0.compose(module_0.parse('\n    This is a test docstring.\n\n    Parameters\n    ----------\n    param1 : int\n        This is a test parameter.\n    param2 : str\n        This is another test parameter.\n    '))
    assert 'Parameters' in docstring


def test_example_f8d2rm3j():
    import numpydoc as module_0
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Yields\n    ------\n    int\n        This is a test yield value.\n    ')
    assert docstring.many_returns[0].is_generator


