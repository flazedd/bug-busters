# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
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
        "parameter",
        "argument",
        "param",
        "attribute",
        "key",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
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
    auto_0 = module_1.auto()
    assert f"{type(auto_0).__module__}.{type(auto_0).__qualname__}" == "enum.auto"
    assert (
        f"{type(module_1.auto.value).__module__}.{type(module_1.auto.value).__qualname__}"
        == "builtins.object"
    )
    docstring_raises_0 = module_0.DocstringRaises(auto_0, auto_0, auto_0)
    assert (
        f"{type(docstring_raises_0).__module__}.{type(docstring_raises_0).__qualname__}"
        == "common.DocstringRaises"
    )
    assert (
        f"{type(docstring_raises_0.args).__module__}.{type(docstring_raises_0.args).__qualname__}"
        == "enum.auto"
    )
    assert (
        f"{type(docstring_raises_0.description).__module__}.{type(docstring_raises_0.description).__qualname__}"
        == "enum.auto"
    )
    assert (
        f"{type(docstring_raises_0.type_name).__module__}.{type(docstring_raises_0.type_name).__qualname__}"
        == "enum.auto"
    )
    assert module_0.PARAM_KEYWORDS == {
        "parameter",
        "argument",
        "param",
        "attribute",
        "key",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}


def test_case_2():
    str_0 = "@0F@eGZi"
    list_0 = [str_0]
    str_1 = "O+q\t({\r1H7E!"
    docstring_param_0 = module_0.DocstringParam(
        list_0, list_0, str_1, str_0, list_0, str_1
    )
    assert (
        f"{type(docstring_param_0).__module__}.{type(docstring_param_0).__qualname__}"
        == "common.DocstringParam"
    )
    assert docstring_param_0.args == ["@0F@eGZi"]
    assert docstring_param_0.description == ["@0F@eGZi"]
    assert docstring_param_0.arg_name == "O+q\t({\r1H7E!"
    assert docstring_param_0.type_name == "@0F@eGZi"
    assert docstring_param_0.is_optional == ["@0F@eGZi"]
    assert docstring_param_0.default == "O+q\t({\r1H7E!"
    assert module_0.PARAM_KEYWORDS == {
        "parameter",
        "argument",
        "param",
        "attribute",
        "key",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    parse_error_0 = module_0.ParseError()
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "common.ParseError"
    )


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
        "parameter",
        "argument",
        "param",
        "attribute",
        "key",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}


def test_case_4():
    list_0 = []
    none_type_0 = None
    docstring_deprecated_0 = module_0.DocstringDeprecated(list_0, list_0, none_type_0)
    assert (
        f"{type(docstring_deprecated_0).__module__}.{type(docstring_deprecated_0).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert docstring_deprecated_0.args == []
    assert docstring_deprecated_0.description == []
    assert docstring_deprecated_0.version is None
    assert module_0.PARAM_KEYWORDS == {
        "parameter",
        "argument",
        "param",
        "attribute",
        "key",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}


def test_case_5():
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
        "parameter",
        "argument",
        "param",
        "attribute",
        "key",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
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
    list_0 = []
    none_type_0 = None
    parse_error_0 = module_0.ParseError()
    assert (
        f"{type(parse_error_0).__module__}.{type(parse_error_0).__qualname__}"
        == "common.ParseError"
    )
    docstring_meta_0 = module_0.DocstringMeta(list_0, list_0)
    assert (
        f"{type(docstring_meta_0).__module__}.{type(docstring_meta_0).__qualname__}"
        == "common.DocstringMeta"
    )
    assert docstring_meta_0.args == []
    assert docstring_meta_0.description == []
    docstring_example_0 = module_0.DocstringExample(list_0, none_type_0, docstring_0)
    assert (
        f"{type(docstring_example_0).__module__}.{type(docstring_example_0).__qualname__}"
        == "common.DocstringExample"
    )
    assert docstring_example_0.args == []
    assert (
        f"{type(docstring_example_0.description).__module__}.{type(docstring_example_0.description).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_example_0.snippet is None
    docstring_meta_1 = module_0.DocstringMeta(docstring_0, none_type_0)
    assert (
        f"{type(docstring_meta_1).__module__}.{type(docstring_meta_1).__qualname__}"
        == "common.DocstringMeta"
    )
    assert (
        f"{type(docstring_meta_1.args).__module__}.{type(docstring_meta_1.args).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_meta_1.description is None
