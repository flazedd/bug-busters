import common as module_0
import typing
import pytest
import enum
def test_example_j19o15lr():
    docstring = module_0.Docstring()
    docstring.short_description = 'This is a short description'
    docstring.long_description = 'This is a long description'
    docstring.blank_after_short_description = True
    param = module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')
    docstring.meta.append(param)
    assert docstring.description == 'This is a short description\n\nThis is a long description'
    assert len(docstring.params) == 1





def test_example_ztc1l6fz():
    docstring = module_0.Docstring()
    assert docstring.style is None


def test_example_ivqiqcza():
    docstring_meta = module_0.DocstringMeta(['arg'], 'description')
    assert docstring_meta.args == ['arg']


def test_example_dlx558q6():
    docstring_param = module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')
    assert docstring_param.arg_name == 'arg_name'


def test_example_c8futuqp():
    docstring_returns = module_0.DocstringReturns(['return'], 'description', 'type_name', True)
    assert docstring_returns.is_generator == True


def test_example_2k9jk6l9():
    docstring_deprecated = module_0.DocstringDeprecated(['deprecated'], 'description', 'version')
    assert docstring_deprecated.version == 'version'


def test_example_u78gk6m4():
    docstring_example = module_0.DocstringExample(['example'], 'snippet', 'description')
    assert docstring_example.snippet == 'snippet'


def test_example_45sjsi28():
    docstring = module_0.Docstring()
    docstring.short_description = 'short description'
    assert docstring.description == 'short description'


