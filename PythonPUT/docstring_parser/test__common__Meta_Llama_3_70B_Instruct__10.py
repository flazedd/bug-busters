import common as module_0
import typing
import enum
import pytest
def test_example_cmlopo4c():
    assert isinstance(module_0.DocstringStyle, enum.EnumMeta)


def test_example_q8dacd33():
    docstring = module_0.Docstring()
    assert docstring.params == []


def test_example_4dgur5lz():
    meta = module_0.DocstringMeta(['arg'], 'description')
    assert meta.description == 'description'


def test_example_v5o906vk():
    param = module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')
    assert param.arg_name == 'arg_name'


def test_example_7ltayr5z():
    raises = module_0.DocstringRaises(['arg'], 'description', 'type_name')
    assert raises.type_name == 'type_name'


def test_example_iqm5v2ig():
    example = module_0.DocstringExample(['arg'], 'snippet', 'description')
    assert example.snippet == 'snippet'


def test_example_74n6gxpd():
    docstring = module_0.Docstring()
    docstring.short_description = 'short description'
    assert docstring.description == 'short description'


def test_example_s7grautw():
    docstring = module_0.Docstring()
    docstring.meta = [module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')]
    assert len(docstring.params) == 1


