import pytest
import enum
import common as module_0
import typing
def test_example_shb52m3d():
    docstring = module_0.Docstring()
    docstring.short_description = 'This is a short description'
    docstring.long_description = 'This is a long description'
    docstring.blank_after_short_description = True
    docstring.meta.append(module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default'))
    docstring.meta.append(module_0.DocstringReturns(['return'], 'description', 'type_name', True))
    docstring.meta.append(module_0.DocstringRaises(['raises'], 'description', 'type_name'))
    docstring.meta.append(module_0.DocstringDeprecated(['deprecation'], 'description', 'version'))
    docstring.meta.append(module_0.DocstringExample(['example'], 'snippet', 'description'))
    assert docstring.description == 'This is a short description\n\nThis is a long description'
    assert len(docstring.params) == 1
    assert len(docstring.raises) == 1
    assert docstring.returns is not None
    assert docstring.deprecation is not None
    assert len(docstring.examples) == 1


def test_example_5llrceyr():
    docstring = module_0.Docstring(style=module_0.DocstringStyle.GOOGLE)
    docstring.short_description = 'This is a short description'
    docstring.meta.append(module_0.DocstringParam(['arg1', 'arg2'], 'description', 'arg_name', 'type_name', True, 'default'))
    docstring.meta.append(module_0.DocstringReturns(['return'], 'description', 'type_name', True))
    docstring.meta.append(module_0.DocstringRaises(['raises'], 'description', 'type_name'))
    docstring.meta.append(module_0.DocstringExample(['example'], 'snippet', 'description'))
    assert docstring.style == module_0.DocstringStyle.GOOGLE
    assert len(docstring.params) == 1
    assert docstring.params[0].arg_name == 'arg_name'
    assert docstring.params[0].type_name == 'type_name'
    assert docstring.params[0].is_optional == True
    assert docstring.params[0].default == 'default'


def test_example_5fw4mvoc():
    docstring = module_0.Docstring()
    docstring.short_description = 'This is a short description'
    docstring.long_description = 'This is a long description'
    docstring.meta.append(module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', False, None))
    docstring.meta.append(module_0.DocstringReturns(['return'], 'description', 'type_name', False))
    assert docstring.params[0].is_optional == False
    assert docstring.returns.is_generator == False


def test_example_1i9jz1my():
    docstring = module_0.Docstring()
    docstring.meta.append(module_0.DocstringRaises(['raises1', 'raises2'], 'description', 'type_name'))
    docstring.meta.append(module_0.DocstringRaises(['raises3'], 'description', 'type_name'))
    assert len(docstring.raises) == 2
    assert docstring.raises[0].args == ['raises1', 'raises2']
    assert docstring.raises[1].args == ['raises3']


def test_example_kb0y2s9l():
    docstring = module_0.Docstring()
    docstring.meta.append(module_0.DocstringParam(['arg1', 'arg2'], 'description', 'arg_name', 'type_name', True, 'default'))
    docstring.meta.append(module_0.DocstringParam(['arg3'], 'description', 'arg_name', 'type_name', False, None))
    assert len(docstring.params) == 2
    assert docstring.params[0].args == ['arg1', 'arg2']
    assert docstring.params[1].args == ['arg3']


def test_example_oy4opwgu():
    docstring = module_0.Docstring()
    docstring.meta.append(module_0.DocstringReturns(['return'], 'description', 'type_name', False))
    docstring.meta.append(module_0.DocstringReturns(['yield'], 'description', 'type_name', True))
    assert len(docstring.many_returns) == 2
    assert docstring.many_returns[0].is_generator == False
    assert docstring.many_returns[1].is_generator == True


def test_example_pd8415ac():
    docstring = module_0.Docstring()
    docstring.short_description = 'This is a short description'
    docstring.long_description = 'This is a long description'
    docstring.meta.append(module_0.DocstringDeprecated(['deprecation'], 'description', 'version'))
    docstring.meta.append(module_0.DocstringExample(['example'], 'snippet', 'description'))
    assert docstring.deprecation.version == 'version'
    assert docstring.examples[0].snippet == 'snippet'


def test_example_9z1ockkv():
    docstring = module_0.Docstring()
    docstring.meta.append(module_0.DocstringParam(['arg1'], 'description', 'arg_name', 'type_name', True, 'default'))
    docstring.meta.append(module_0.DocstringParam(['arg2'], 'description', 'arg_name', 'type_name', False, None))
    assert len(docstring.params) == 2
    assert docstring.params[0].is_optional == True
    assert docstring.params[1].is_optional == False


