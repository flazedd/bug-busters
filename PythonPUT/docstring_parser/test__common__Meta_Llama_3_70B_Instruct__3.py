import enum
import common as module_0
import typing
import pytest
def test_example_5whnwyw3():
    assert isinstance(module_0.DocstringStyle, enum.EnumMeta)


def test_example_zybaxmrg():
    meta = module_0.DocstringMeta(args=['arg'], description='description')
    assert meta.args == ['arg']
    assert meta.description == 'description'


def test_example_lxc6v6co():
    param = module_0.DocstringParam(args=['arg'], description='description', arg_name='arg_name', type_name='type_name', is_optional=True, default='default')
    assert param.arg_name == 'arg_name'
    assert param.type_name == 'type_name'
    assert param.is_optional == True
    assert param.default == 'default'


def test_example_zhqwkrqh():
    returns = module_0.DocstringReturns(args=['return'], description='description', type_name='type_name', is_generator=True, return_name='return_name')
    assert returns.type_name == 'type_name'
    assert returns.is_generator == True
    assert returns.return_name == 'return_name'


def test_example_3rexnv61():
    raises = module_0.DocstringRaises(args=['exception'], description='description', type_name='type_name')
    assert raises.type_name == 'type_name'
    assert raises.description == 'description'


def test_example_sf46zpl7():
    deprecated = module_0.DocstringDeprecated(args=['deprecation'], description='description', version='version')
    assert deprecated.version == 'version'
    assert deprecated.description == 'description'


def test_example_1ph6y4xx():
    example = module_0.DocstringExample(args=['example'], snippet='snippet', description='description')
    assert example.snippet == 'snippet'
    assert example.description == 'description'


def test_example_qu0uofjr():
    docstring = module_0.Docstring()
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert docstring.blank_after_short_description is False
    assert docstring.blank_after_long_description is False
    assert docstring.meta == []
    assert docstring.style is None


