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
def test_example_yznkfkka():
    text = 'This is a test docstring.\n\nParameters\n----------\nparam1 : int\n    This is the first parameter.\nparam2 : str\n    This is the second parameter.\n\nReturns\n-------\nint\n    This is the return value.\n\nRaises\n------\nValueError\n    If something goes wrong.\n'
    parser = module_0.NumpydocParser()
    docstring = parser.parse(text)
    assert isinstance(docstring, module_0.Docstring)


def test_example_pndgzhfm():
    text = 'This is a test docstring.\n\nExamples\n--------\n>>> import numpy.matlib\n>>> np.matlib.empty((2, 2))    # filled with random data\nmatrix([[  6.76425276e-320,   9.79033856e-307], # random\n        [  7.39337286e-309,   3.22135945e-309]])\n>>> np.matlib.empty((2, 2), dtype=int)\nmatrix([[ 6600475,        0], # random\n        [ 6586976, 22740995]])\n'
    parser = module_0.NumpydocParser()
    docstring = parser.parse(text)
    assert len(docstring.examples) == 2


def test_example_qh9dj9l4():
    text = 'This is a test docstring.\n\nParameters\n----------\nparam1 : int\n    This is the first parameter.\nparam2 : str\n    This is the second parameter.\n\nReturns\n-------\nint\n    This is the return value.\n'
    parser = module_0.NumpydocParser()
    docstring = parser.parse(text)
    assert len(docstring.params) == 2


def test_example_ntdzeqjl():
    text = 'This is a test docstring.\n\nWarnings\n--------\nThis is a warning.\n'
    parser = module_0.NumpydocParser()
    docstring = parser.parse(text)
    assert len(docstring.meta) == 1


def test_example_pktpbnc2():
    text = 'This is a test docstring.\n\nNotes\n-----\nThis is a note.\n'
    parser = module_0.NumpydocParser()
    docstring = parser.parse(text)
    assert len(docstring.meta) == 1


def test_example_pb4i60ns():
    text = 'This is a test docstring.\n\nReferences\n----------\nSomething : https://example.com\n'
    parser = module_0.NumpydocParser()
    docstring = parser.parse(text)
    assert len(docstring.meta) == 1


def test_example_kjmaytco():
    text = 'This is a test docstring.\n\nAttributes\n----------\nattr1 : int\n    This is the first attribute.\nattr2 : str\n    This is the second attribute.\n'
    parser = module_0.NumpydocParser()
    docstring = parser.parse(text)
    assert len([item for item in docstring.params if item.args[0] == 'attribute']) == 2


def test_example_6g7ow8s8():
    text = 'This is a test docstring.\n\nReceives\n--------\nrecv1 : int\n    This is the first receive.\nrecv2 : str\n    This is the second receive.\n'
    parser = module_0.NumpydocParser()
    docstring = parser.parse(text)
    assert len([item for item in docstring.params if item.args[0] == 'receives']) == 2


