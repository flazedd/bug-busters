# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import common as module_0
import enum as module_1


def test_case_0():
    parse_error_0 = module_0.ParseError()
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "common.ParseError"
    )
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "arg",
        "key",
        "param",
        "attribute",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}


def test_case_1():
    bool_0 = True
    none_type_0 = None
    docstring_raises_0 = module_0.DocstringRaises(bool_0, none_type_0, none_type_0)
    assert (
        f"{type(docstring_raises_0).__module__}.{type(docstring_raises_0).__qualname__}"
        == "common.DocstringRaises"
    )
    assert docstring_raises_0.args is True
    assert docstring_raises_0.description is None
    assert docstring_raises_0.type_name is None
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "arg",
        "key",
        "param",
        "attribute",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ",(d/-./&d wi4"
    str_1 = "#!%*Q^G?SB9(CHa|0>Z"
    list_0 = [str_0, str_1]
    docstring_param_0 = module_0.DocstringParam(
        list_0, str_1, str_1, str_1, list_0, str_0
    )
    assert (
        f"{type(docstring_param_0).__module__}.{type(docstring_param_0).__qualname__}"
        == "common.DocstringParam"
    )
    assert docstring_param_0.args == [",(d/-./&d wi4", "#!%*Q^G?SB9(CHa|0>Z"]
    assert docstring_param_0.description == "#!%*Q^G?SB9(CHa|0>Z"
    assert docstring_param_0.arg_name == "#!%*Q^G?SB9(CHa|0>Z"
    assert docstring_param_0.type_name == "#!%*Q^G?SB9(CHa|0>Z"
    assert docstring_param_0.is_optional == [",(d/-./&d wi4", "#!%*Q^G?SB9(CHa|0>Z"]
    assert docstring_param_0.default == ",(d/-./&d wi4"
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "arg",
        "key",
        "param",
        "attribute",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
    module_1.EnumMeta()


def test_case_3():
    none_type_0 = None
    bool_0 = True
    docstring_returns_0 = module_0.DocstringReturns(
        none_type_0, none_type_0, none_type_0, bool_0, none_type_0
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
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "arg",
        "key",
        "param",
        "attribute",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}


def test_case_4():
    parse_error_0 = module_0.ParseError()
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "common.ParseError"
    )
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "arg",
        "key",
        "param",
        "attribute",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
    list_0 = [parse_error_0, parse_error_0]
    docstring_deprecated_0 = module_0.DocstringDeprecated(list_0, list_0, parse_error_0)
    assert (
        f"{type(docstring_deprecated_0).__module__}.{type(docstring_deprecated_0).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert (
        f"{type(docstring_deprecated_0.args).__module__}.{type(docstring_deprecated_0.args).__qualname__}"
        == "builtins.list"
    )
    assert len(docstring_deprecated_0.args) == 2
    assert (
        f"{type(docstring_deprecated_0.description).__module__}.{type(docstring_deprecated_0.description).__qualname__}"
        == "builtins.list"
    )
    assert len(docstring_deprecated_0.description) == 2
    assert (
        f"{type(docstring_deprecated_0.version).__module__}.{type(docstring_deprecated_0.version).__qualname__}"
        == "common.ParseError"
    )


def test_case_5():
    str_0 = "n2z9U`,"
    list_0 = [str_0]
    str_1 = "f0VT8b"
    docstring_example_0 = module_0.DocstringExample(list_0, str_0, str_1)
    assert (
        f"{type(docstring_example_0).__module__}.{type(docstring_example_0).__qualname__}"
        == "common.DocstringExample"
    )
    assert docstring_example_0.args == ["n2z9U`,"]
    assert docstring_example_0.description == "f0VT8b"
    assert docstring_example_0.snippet == "n2z9U`,"
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "arg",
        "key",
        "param",
        "attribute",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
    none_type_0 = None
    docstring_deprecated_0 = module_0.DocstringDeprecated(
        none_type_0, none_type_0, none_type_0
    )
    assert (
        f"{type(docstring_deprecated_0).__module__}.{type(docstring_deprecated_0).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert docstring_deprecated_0.args is None
    assert docstring_deprecated_0.description is None
    assert docstring_deprecated_0.version is None


def test_case_6():
    parse_error_0 = module_0.ParseError()
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "common.ParseError"
    )
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "arg",
        "key",
        "param",
        "attribute",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
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
    complex_0 = -2327.6 + 2401j
    none_type_0 = None
    parse_error_1 = module_0.ParseError()
    assert (
        f"{type(parse_error_1).__module__}.{type(parse_error_1).__qualname__}"
        == "common.ParseError"
    )
    parse_error_2 = module_0.ParseError()
    assert (
        f"{type(parse_error_2).__module__}.{type(parse_error_2).__qualname__}"
        == "common.ParseError"
    )
    docstring_meta_0 = module_0.DocstringMeta(none_type_0, none_type_0)
    assert (
        f"{type(docstring_meta_0).__module__}.{type(docstring_meta_0).__qualname__}"
        == "common.DocstringMeta"
    )
    assert docstring_meta_0.args is None
    assert docstring_meta_0.description is None
    docstring_example_0 = module_0.DocstringExample(complex_0, complex_0, none_type_0)
    assert (
        f"{type(docstring_example_0).__module__}.{type(docstring_example_0).__qualname__}"
        == "common.DocstringExample"
    )
    assert docstring_example_0.args == (-2327.6 + 2401j)
    assert docstring_example_0.description is None
    assert docstring_example_0.snippet == (-2327.6 + 2401j)
