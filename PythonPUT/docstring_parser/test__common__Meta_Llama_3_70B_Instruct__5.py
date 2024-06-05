import pytest
import typing
import common as module_0
import enum
def test_example_qmahct3c():
    assert isinstance(module_0.DocstringStyle, enum.EnumMeta)


def test_example_6xn1a75w():
    assert module_0.RETURNS_KEYWORDS == {'return', 'returns'}


def test_example_hmh6o5la():
    assert issubclass(module_0.DocstringParam, module_0.DocstringMeta)


def test_example_38b4k9od():
    assert module_0.DocstringMeta.__init__.__code__.co_argcount == 3


def test_example_ocauljw8():
    docstring = module_0.Docstring()
    assert docstring.meta == []


def test_example_bcb2712u():
    assert module_0.PARAM_KEYWORDS == {'param', 'parameter', 'arg', 'argument', 'attribute', 'key', 'keyword'}


def test_example_0utwy5g6():
    docstring = module_0.Docstring()
    assert docstring.short_description is None


def test_example_9jv30fr7():
    assert module_0.DocstringRaises.__init__.__code__.co_argcount == 4


