import common as module_0
import pytest
import enum
import typing as T
def test_example():
    assert isinstance(module_0.DocstringStyle.REST, enum.Enum)


def test_example():
    docstring = module_0.Docstring()
    assert docstring.meta == []


