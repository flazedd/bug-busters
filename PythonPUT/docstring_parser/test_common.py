# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import common as module_0


def test_case_0():
    parse_error_0 = module_0.ParseError()
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "common.ParseError"
    )
    assert module_0.PARAM_KEYWORDS == {
        "key",
        "param",
        "keyword",
        "attribute",
        "argument",
        "parameter",
        "arg",
    }
    assert module_0.RAISES_KEYWORDS == {"exception", "except", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}


def test_case_1():
    float_0 = 1566.037
    docstring_meta_0 = module_0.DocstringMeta(float_0, float_0)
    assert (
        f"{type(docstring_meta_0).__module__}.{type(docstring_meta_0).__qualname__}"
        == "common.DocstringMeta"
    )
    assert docstring_meta_0.args == pytest.approx(1566.037, abs=0.01, rel=0.01)
    assert docstring_meta_0.description == pytest.approx(1566.037, abs=0.01, rel=0.01)
    assert module_0.PARAM_KEYWORDS == {
        "key",
        "param",
        "keyword",
        "attribute",
        "argument",
        "parameter",
        "arg",
    }
    assert module_0.RAISES_KEYWORDS == {"exception", "except", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}


def test_case_2():
    float_0 = 1577.54111
    none_type_0 = None
    str_0 = ""
    docstring_param_0 = module_0.DocstringParam(
        none_type_0, str_0, none_type_0, str_0, none_type_0, none_type_0
    )
    assert (
        f"{type(docstring_param_0).__module__}.{type(docstring_param_0).__qualname__}"
        == "common.DocstringParam"
    )
    assert docstring_param_0.args is None
    assert docstring_param_0.description == ""
    assert docstring_param_0.arg_name is None
    assert docstring_param_0.type_name == ""
    assert docstring_param_0.is_optional is None
    assert docstring_param_0.default is None
    assert module_0.PARAM_KEYWORDS == {
        "key",
        "param",
        "keyword",
        "attribute",
        "argument",
        "parameter",
        "arg",
    }
    assert module_0.RAISES_KEYWORDS == {"exception", "except", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
    docstring_meta_0 = module_0.DocstringMeta(float_0, float_0)
    assert (
        f"{type(docstring_meta_0).__module__}.{type(docstring_meta_0).__qualname__}"
        == "common.DocstringMeta"
    )
    assert docstring_meta_0.args == pytest.approx(1577.54111, abs=0.01, rel=0.01)
    assert docstring_meta_0.description == pytest.approx(1577.54111, abs=0.01, rel=0.01)


def test_case_3():
    parse_error_0 = module_0.ParseError()
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "common.ParseError"
    )
    assert module_0.PARAM_KEYWORDS == {
        "key",
        "param",
        "keyword",
        "attribute",
        "argument",
        "parameter",
        "arg",
    }
    assert module_0.RAISES_KEYWORDS == {"exception", "except", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
    bool_0 = True
    docstring_returns_0 = module_0.DocstringReturns(
        parse_error_0, parse_error_0, parse_error_0, bool_0
    )
    assert (
        f"{type(docstring_returns_0).__module__}.{type(docstring_returns_0).__qualname__}"
        == "common.DocstringReturns"
    )
    assert (
        f"{type(docstring_returns_0.args).__module__}.{type(docstring_returns_0.args).__qualname__}"
        == "common.ParseError"
    )
    assert (
        f"{type(docstring_returns_0.description).__module__}.{type(docstring_returns_0.description).__qualname__}"
        == "common.ParseError"
    )
    assert (
        f"{type(docstring_returns_0.type_name).__module__}.{type(docstring_returns_0.type_name).__qualname__}"
        == "common.ParseError"
    )
    assert docstring_returns_0.is_generator is True
    assert docstring_returns_0.return_name is None


def test_case_4():
    str_0 = "f2oNESzYG}3I76J"
    str_1 = ';Vvoi"\n$>!*4D ~47;2'
    list_0 = [str_0, str_1, str_1]
    docstring_raises_0 = module_0.DocstringRaises(list_0, str_0, str_1)
    assert (
        f"{type(docstring_raises_0).__module__}.{type(docstring_raises_0).__qualname__}"
        == "common.DocstringRaises"
    )
    assert docstring_raises_0.args == [
        "f2oNESzYG}3I76J",
        ';Vvoi"\n$>!*4D ~47;2',
        ';Vvoi"\n$>!*4D ~47;2',
    ]
    assert docstring_raises_0.description == "f2oNESzYG}3I76J"
    assert docstring_raises_0.type_name == ';Vvoi"\n$>!*4D ~47;2'
    assert module_0.PARAM_KEYWORDS == {
        "key",
        "param",
        "keyword",
        "attribute",
        "argument",
        "parameter",
        "arg",
    }
    assert module_0.RAISES_KEYWORDS == {"exception", "except", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}


@pytest.mark.xfail(strict=True)
def test_case_5():
    parse_error_0 = module_0.ParseError()
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "common.ParseError"
    )
    assert module_0.PARAM_KEYWORDS == {
        "key",
        "param",
        "keyword",
        "attribute",
        "argument",
        "parameter",
        "arg",
    }
    assert module_0.RAISES_KEYWORDS == {"exception", "except", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_0 = "r4DBr_\nrQLws8,Ms;\n$"
    list_0 = [str_0, str_0, str_0, str_0]
    none_type_0 = None
    docstring_deprecated_0 = module_0.DocstringDeprecated(
        none_type_0, str_0, none_type_0
    )
    assert (
        f"{type(docstring_deprecated_0).__module__}.{type(docstring_deprecated_0).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert docstring_deprecated_0.args is None
    assert docstring_deprecated_0.description == "r4DBr_\nrQLws8,Ms;\n$"
    assert docstring_deprecated_0.version is None
    docstring_meta_0 = module_0.DocstringMeta(list_0, str_0)
    assert (
        f"{type(docstring_meta_0).__module__}.{type(docstring_meta_0).__qualname__}"
        == "common.DocstringMeta"
    )
    assert docstring_meta_0.args == [
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
    ]
    assert docstring_meta_0.description == "r4DBr_\nrQLws8,Ms;\n$"
    parse_error_1 = module_0.ParseError()
    assert (
        f"{type(parse_error_1).__module__}.{type(parse_error_1).__qualname__}"
        == "common.ParseError"
    )
    docstring_returns_0 = module_0.DocstringReturns(
        list_0, list_0, docstring_meta_0, str_0
    )
    assert (
        f"{type(docstring_returns_0).__module__}.{type(docstring_returns_0).__qualname__}"
        == "common.DocstringReturns"
    )
    assert docstring_returns_0.args == [
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
    ]
    assert docstring_returns_0.description == [
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
    ]
    assert (
        f"{type(docstring_returns_0.type_name).__module__}.{type(docstring_returns_0.type_name).__qualname__}"
        == "common.DocstringMeta"
    )
    assert docstring_returns_0.is_generator == "r4DBr_\nrQLws8,Ms;\n$"
    assert docstring_returns_0.return_name is None
    docstring_returns_1 = module_0.DocstringReturns(
        list_0, str_0, str_0, docstring_deprecated_0
    )
    assert (
        f"{type(docstring_returns_1).__module__}.{type(docstring_returns_1).__qualname__}"
        == "common.DocstringReturns"
    )
    assert docstring_returns_1.args == [
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
    ]
    assert docstring_returns_1.description == "r4DBr_\nrQLws8,Ms;\n$"
    assert docstring_returns_1.type_name == "r4DBr_\nrQLws8,Ms;\n$"
    assert (
        f"{type(docstring_returns_1.is_generator).__module__}.{type(docstring_returns_1.is_generator).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert docstring_returns_1.return_name is None
    docstring_deprecated_1 = module_0.DocstringDeprecated(
        list_0, none_type_0, docstring_deprecated_0
    )
    assert (
        f"{type(docstring_deprecated_1).__module__}.{type(docstring_deprecated_1).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert docstring_deprecated_1.args == [
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
    ]
    assert docstring_deprecated_1.description is None
    assert (
        f"{type(docstring_deprecated_1.version).__module__}.{type(docstring_deprecated_1.version).__qualname__}"
        == "common.DocstringDeprecated"
    )
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
    str_1 = ""
    docstring_param_0 = module_0.DocstringParam(
        list_0, none_type_0, str_1, none_type_0, parse_error_0, none_type_0
    )
    assert (
        f"{type(docstring_param_0).__module__}.{type(docstring_param_0).__qualname__}"
        == "common.DocstringParam"
    )
    assert docstring_param_0.args == [
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
        "r4DBr_\nrQLws8,Ms;\n$",
    ]
    assert docstring_param_0.description is None
    assert docstring_param_0.arg_name == ""
    assert docstring_param_0.type_name is None
    assert (
        f"{type(docstring_param_0.is_optional).__module__}.{type(docstring_param_0.is_optional).__qualname__}"
        == "common.ParseError"
    )
    assert docstring_param_0.default is None
    module_0.ParseError(**list_0)


def test_case_6():
    str_0 = "`\\MM\x0b"
    str_1 = "3NPA:zftH)"
    docstring_style_0 = module_0.DocstringStyle.REST
    docstring_example_0 = module_0.DocstringExample(str_1, docstring_style_0, str_1)
    assert (
        f"{type(docstring_example_0).__module__}.{type(docstring_example_0).__qualname__}"
        == "common.DocstringExample"
    )
    assert docstring_example_0.args == "3NPA:zftH)"
    assert docstring_example_0.description == "3NPA:zftH)"
    assert docstring_example_0.snippet == module_0.DocstringStyle.REST
    assert module_0.PARAM_KEYWORDS == {
        "key",
        "param",
        "keyword",
        "attribute",
        "argument",
        "parameter",
        "arg",
    }
    assert module_0.RAISES_KEYWORDS == {"exception", "except", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
    list_0 = [str_0, str_1]
    docstring_example_1 = module_0.DocstringExample(list_0, str_0, str_1)
    assert (
        f"{type(docstring_example_1).__module__}.{type(docstring_example_1).__qualname__}"
        == "common.DocstringExample"
    )
    assert docstring_example_1.args == ["`\\MM\x0b", "3NPA:zftH)"]
    assert docstring_example_1.description == "3NPA:zftH)"
    assert docstring_example_1.snippet == "`\\MM\x0b"


def test_case_7():
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
        "key",
        "param",
        "keyword",
        "attribute",
        "argument",
        "parameter",
        "arg",
    }
    assert module_0.RAISES_KEYWORDS == {"exception", "except", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
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
