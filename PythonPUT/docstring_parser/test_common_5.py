# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import common as module_0
import enum as module_1


def test_case_0():
    docstring_0 = module_0.Docstring()
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description is None
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style is None
    assert module_0.PARAM_KEYWORDS == {
        "arg",
        "argument",
        "param",
        "parameter",
        "attribute",
        "keyword",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "exception", "except", "raise"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    assert (
        f"{type(module_0.Docstring.description).__module__}.{type(module_0.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.params).__module__}.{type(module_0.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.raises).__module__}.{type(module_0.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.returns).__module__}.{type(module_0.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.many_returns).__module__}.{type(module_0.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.deprecation).__module__}.{type(module_0.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.examples).__module__}.{type(module_0.Docstring.examples).__qualname__}"
        == "builtins.property"
    )


def test_case_1():
    list_0 = []
    none_type_0 = None
    docstring_example_0 = module_0.DocstringExample(list_0, list_0, none_type_0)
    assert (
        f"{type(docstring_example_0).__module__}.{type(docstring_example_0).__qualname__}"
        == "common.DocstringExample"
    )
    assert docstring_example_0.args == []
    assert docstring_example_0.description is None
    assert docstring_example_0.snippet == []
    assert module_0.PARAM_KEYWORDS == {
        "arg",
        "argument",
        "param",
        "parameter",
        "attribute",
        "keyword",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "exception", "except", "raise"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}


def test_case_2():
    str_0 = ")23(A/Bl"
    str_1 = "G;8%A/@'cm\t* avP\""
    list_0 = [str_0, str_1]
    none_type_0 = None
    docstring_param_0 = module_0.DocstringParam(
        list_0, none_type_0, str_0, list_0, none_type_0, str_0
    )
    assert (
        f"{type(docstring_param_0).__module__}.{type(docstring_param_0).__qualname__}"
        == "common.DocstringParam"
    )
    assert docstring_param_0.args == [")23(A/Bl", "G;8%A/@'cm\t* avP\""]
    assert docstring_param_0.description is None
    assert docstring_param_0.arg_name == ")23(A/Bl"
    assert docstring_param_0.type_name == [")23(A/Bl", "G;8%A/@'cm\t* avP\""]
    assert docstring_param_0.is_optional is None
    assert docstring_param_0.default == ")23(A/Bl"
    assert module_0.PARAM_KEYWORDS == {
        "arg",
        "argument",
        "param",
        "parameter",
        "attribute",
        "keyword",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "exception", "except", "raise"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    list_1 = [str_0]
    docstring_deprecated_0 = module_0.DocstringDeprecated(list_1, str_0, str_0)
    assert (
        f"{type(docstring_deprecated_0).__module__}.{type(docstring_deprecated_0).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert docstring_deprecated_0.args == [")23(A/Bl"]
    assert docstring_deprecated_0.description == ")23(A/Bl"
    assert docstring_deprecated_0.version == ")23(A/Bl"


def test_case_3():
    none_type_0 = None
    bool_0 = False
    docstring_param_0 = module_0.DocstringParam(
        none_type_0, none_type_0, bool_0, bool_0, bool_0, none_type_0
    )
    assert (
        f"{type(docstring_param_0).__module__}.{type(docstring_param_0).__qualname__}"
        == "common.DocstringParam"
    )
    assert docstring_param_0.args is None
    assert docstring_param_0.description is None
    assert docstring_param_0.arg_name is False
    assert docstring_param_0.type_name is False
    assert docstring_param_0.is_optional is False
    assert docstring_param_0.default is None
    assert module_0.PARAM_KEYWORDS == {
        "arg",
        "argument",
        "param",
        "parameter",
        "attribute",
        "keyword",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "exception", "except", "raise"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    bool_1 = True
    docstring_0 = module_0.Docstring()
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description is None
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style is None
    assert (
        f"{type(module_0.Docstring.description).__module__}.{type(module_0.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.params).__module__}.{type(module_0.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.raises).__module__}.{type(module_0.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.returns).__module__}.{type(module_0.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.many_returns).__module__}.{type(module_0.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.deprecation).__module__}.{type(module_0.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Docstring.examples).__module__}.{type(module_0.Docstring.examples).__qualname__}"
        == "builtins.property"
    )
    docstring_returns_0 = module_0.DocstringReturns(
        none_type_0, none_type_0, none_type_0, bool_1, none_type_0
    )
    assert (
        f"{type(docstring_returns_0).__module__}.{type(docstring_returns_0).__qualname__}"
        == "common.DocstringReturns"
    )
    assert docstring_returns_0.args is None
    assert docstring_returns_0.description is None
    assert docstring_returns_0.type_name is None
    assert docstring_returns_0.is_generator is True
    assert docstring_returns_0.return_name is None


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    str_0 = "i?UsAf"
    list_0 = [str_0]
    docstring_param_0 = module_0.DocstringParam(
        list_0, none_type_0, list_0, none_type_0, none_type_0, none_type_0
    )
    assert (
        f"{type(docstring_param_0).__module__}.{type(docstring_param_0).__qualname__}"
        == "common.DocstringParam"
    )
    assert docstring_param_0.args == ["i?UsAf"]
    assert docstring_param_0.description is None
    assert docstring_param_0.arg_name == ["i?UsAf"]
    assert docstring_param_0.type_name is None
    assert docstring_param_0.is_optional is None
    assert docstring_param_0.default is None
    assert module_0.PARAM_KEYWORDS == {
        "arg",
        "argument",
        "param",
        "parameter",
        "attribute",
        "keyword",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "exception", "except", "raise"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    docstring_raises_0 = module_0.DocstringRaises(none_type_0, none_type_0, none_type_0)
    assert (
        f"{type(docstring_raises_0).__module__}.{type(docstring_raises_0).__qualname__}"
        == "common.DocstringRaises"
    )
    assert docstring_raises_0.args is None
    assert docstring_raises_0.description is None
    assert docstring_raises_0.type_name is None
    module_0.ParseError(**none_type_0)


def test_case_5():
    enum_dict_0 = module_1._EnumDict()
    assert (
        f"{type(enum_dict_0).__module__}.{type(enum_dict_0).__qualname__}"
        == "enum._EnumDict"
    )
    assert len(enum_dict_0) == 0
    none_type_0 = None
    docstring_deprecated_0 = module_0.DocstringDeprecated(
        enum_dict_0, none_type_0, enum_dict_0
    )
    assert (
        f"{type(docstring_deprecated_0).__module__}.{type(docstring_deprecated_0).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert (
        f"{type(docstring_deprecated_0.args).__module__}.{type(docstring_deprecated_0.args).__qualname__}"
        == "enum._EnumDict"
    )
    assert len(docstring_deprecated_0.args) == 0
    assert docstring_deprecated_0.description is None
    assert (
        f"{type(docstring_deprecated_0.version).__module__}.{type(docstring_deprecated_0.version).__qualname__}"
        == "enum._EnumDict"
    )
    assert len(docstring_deprecated_0.version) == 0
    assert module_0.PARAM_KEYWORDS == {
        "arg",
        "argument",
        "param",
        "parameter",
        "attribute",
        "keyword",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "exception", "except", "raise"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}