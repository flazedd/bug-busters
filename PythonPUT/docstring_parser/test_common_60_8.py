# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import common as module_0


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
        "argument",
        "parameter",
        "param",
        "keyword",
        "arg",
        "attribute",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
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


def test_case_1():
    str_0 = "-A&#~wa+M\n8lU+"
    list_0 = [str_0, str_0, str_0]
    docstring_deprecated_0 = module_0.DocstringDeprecated(list_0, str_0, list_0)
    assert (
        f"{type(docstring_deprecated_0).__module__}.{type(docstring_deprecated_0).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert docstring_deprecated_0.args == [
        "-A&#~wa+M\n8lU+",
        "-A&#~wa+M\n8lU+",
        "-A&#~wa+M\n8lU+",
    ]
    assert docstring_deprecated_0.description == "-A&#~wa+M\n8lU+"
    assert docstring_deprecated_0.version == [
        "-A&#~wa+M\n8lU+",
        "-A&#~wa+M\n8lU+",
        "-A&#~wa+M\n8lU+",
    ]
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "param",
        "keyword",
        "arg",
        "attribute",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}


def test_case_2():
    bool_0 = False
    none_type_0 = None
    docstring_param_0 = module_0.DocstringParam(
        bool_0, bool_0, bool_0, none_type_0, none_type_0, none_type_0
    )
    assert (
        f"{type(docstring_param_0).__module__}.{type(docstring_param_0).__qualname__}"
        == "common.DocstringParam"
    )
    assert docstring_param_0.args is False
    assert docstring_param_0.description is False
    assert docstring_param_0.arg_name is False
    assert docstring_param_0.type_name is None
    assert docstring_param_0.is_optional is None
    assert docstring_param_0.default is None
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "param",
        "keyword",
        "arg",
        "attribute",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_0 = "g14FipwMcz(ITPlo98>"
    str_1 = "J(/~ 5D}fzf:"
    str_2 = "Pw-\\Rg8F"
    list_0 = [str_0, str_0, str_1, str_2]
    docstring_meta_0 = module_0.DocstringMeta(list_0, str_0)
    assert (
        f"{type(docstring_meta_0).__module__}.{type(docstring_meta_0).__qualname__}"
        == "common.DocstringMeta"
    )
    assert docstring_meta_0.args == [
        "g14FipwMcz(ITPlo98>",
        "g14FipwMcz(ITPlo98>",
        "J(/~ 5D}fzf:",
        "Pw-\\Rg8F",
    ]
    assert docstring_meta_0.description == "g14FipwMcz(ITPlo98>"


def test_case_3():
    int_0 = 1374
    none_type_0 = None
    docstring_deprecated_0 = module_0.DocstringDeprecated(
        int_0, none_type_0, none_type_0
    )
    assert (
        f"{type(docstring_deprecated_0).__module__}.{type(docstring_deprecated_0).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert docstring_deprecated_0.args == 1374
    assert docstring_deprecated_0.description is None
    assert docstring_deprecated_0.version is None
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "param",
        "keyword",
        "arg",
        "attribute",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_0 = '<"VxMwrQd!{('
    str_1 = "?-m9=xHrO"
    list_0 = [str_0, str_1]
    bool_0 = False
    docstring_returns_0 = module_0.DocstringReturns(list_0, str_0, str_0, bool_0)
    assert (
        f"{type(docstring_returns_0).__module__}.{type(docstring_returns_0).__qualname__}"
        == "common.DocstringReturns"
    )
    assert docstring_returns_0.args == ['<"VxMwrQd!{(', "?-m9=xHrO"]
    assert docstring_returns_0.description == '<"VxMwrQd!{('
    assert docstring_returns_0.type_name == '<"VxMwrQd!{('
    assert docstring_returns_0.is_generator is False
    assert docstring_returns_0.return_name is None


def test_case_4():
    str_0 = "=mDfI.o%\t%ib"
    list_0 = [str_0]
    docstring_raises_0 = module_0.DocstringRaises(list_0, str_0, str_0)
    assert (
        f"{type(docstring_raises_0).__module__}.{type(docstring_raises_0).__qualname__}"
        == "common.DocstringRaises"
    )
    assert docstring_raises_0.args == ["=mDfI.o%\t%ib"]
    assert docstring_raises_0.description == "=mDfI.o%\t%ib"
    assert docstring_raises_0.type_name == "=mDfI.o%\t%ib"
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "param",
        "keyword",
        "arg",
        "attribute",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
    list_1 = []
    none_type_0 = None
    docstring_deprecated_0 = module_0.DocstringDeprecated(
        list_1, none_type_0, none_type_0
    )
    assert (
        f"{type(docstring_deprecated_0).__module__}.{type(docstring_deprecated_0).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert docstring_deprecated_0.args == []
    assert docstring_deprecated_0.description is None
    assert docstring_deprecated_0.version is None


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = ""
    str_1 = "K"
    list_0 = [str_0, str_1]
    docstring_example_0 = module_0.DocstringExample(list_0, str_1, str_1)
    assert (
        f"{type(docstring_example_0).__module__}.{type(docstring_example_0).__qualname__}"
        == "common.DocstringExample"
    )
    assert docstring_example_0.args == ["", "K"]
    assert docstring_example_0.description == "K"
    assert docstring_example_0.snippet == "K"
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "parameter",
        "param",
        "keyword",
        "arg",
        "attribute",
        "key",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"example", "examples"}
    module_0.ParseError(*docstring_example_0, **docstring_example_0)
