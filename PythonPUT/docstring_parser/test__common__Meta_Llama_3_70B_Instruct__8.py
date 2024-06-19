import common as module_0
import pytest
import typing
import enum
def test_example_vnhhvv17():
    docstring = module_0.Docstring()
    docstring.short_description = 'This is a short description'
    docstring.long_description = 'This is a long description'
    assert docstring.description == 'This is a short description\nThis is a long description'


def test_example_04y36pjz():
    docstring = module_0.Docstring()
    param = module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')
    docstring.meta.append(param)
    assert len(docstring.params) == 1


def test_example_hetszoo5():
    docstring = module_0.Docstring()
    raises = module_0.DocstringRaises(['ValueError'], 'description', 'type_name')
    docstring.meta.append(raises)
    assert len(docstring.raises) == 1


def test_example_lou4358x():
    docstring = module_0.Docstring()
    returns = module_0.DocstringReturns(['return'], 'description', 'type_name', False)
    docstring.meta.append(returns)
    assert docstring.returns.type_name == 'type_name'


def test_example_9c1avqc2():
    docstring = module_0.Docstring()
    example = module_0.DocstringExample(['example'], 'snippet', 'description')
    docstring.meta.append(example)
    assert len(docstring.examples) == 1


def test_example_38figqyh():
    docstring = module_0.Docstring()
    deprecated = module_0.DocstringDeprecated(['deprecation'], 'description', 'version')
    docstring.meta.append(deprecated)
    assert docstring.deprecation.version == 'version'


def test_example_u2t6x3ah():
    docstring = module_0.Docstring(style=module_0.DocstringStyle.REST)
    assert docstring.style == module_0.DocstringStyle.REST


def test_example_niu4i94o():
    docstring = module_0.Docstring()
    param1 = module_0.DocstringParam(['arg1'], 'description1', 'arg_name1', 'type_name1', True, 'default1')
    param2 = module_0.DocstringParam(['arg2'], 'description2', 'arg_name2', 'type_name2', False, 'default2')
    docstring.meta.append(param1)
    docstring.meta.append(param2)
    assert len(docstring.params) == 2


