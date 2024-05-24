import common as module_0
import enum
import pytest
import typing
def test_example_gv2q6x28():
    assert isinstance(module_0.DocstringStyle.REST, enum.Enum)


def test_example_1yvxxgtd():
    docstring = module_0.Docstring()
    assert docstring.meta == []


def test_example_b9g74lr4():
    docstring = module_0.Docstring()
    assert docstring.short_description is None


def test_example_m92a9tcc():
    docstring_param = module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')
    assert docstring_param.arg_name == 'arg_name'


def test_example_b7n1b0ku():
    docstring_returns = module_0.DocstringReturns(['return'], 'description', 'type_name', True)
    assert docstring_returns.is_generator == True


def test_example_r3xs3yd3():
    docstring = module_0.Docstring()
    assert docstring.description is None


def test_example_dji8ggoi():
    assert module_0.PARAM_KEYWORDS == {'param', 'parameter', 'arg', 'argument', 'attribute', 'key', 'keyword'}


def test_example_iusj9fuh():
    docstring_deprecated = module_0.DocstringDeprecated(['deprecated'], 'description', 'version')
    assert docstring_deprecated.version == 'version'


