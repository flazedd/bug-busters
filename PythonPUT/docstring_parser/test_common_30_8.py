# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import common as module_0


def test_case_0():
    pass


def test_case_1():
    str_0 = "um!lt3J-Yo9JH\t+`"
    list_0 = [str_0, str_0, str_0, str_0]
    docstring_deprecated_0 = module_0.DocstringDeprecated(list_0, str_0, str_0)
    assert (
        f"{type(docstring_deprecated_0).__module__}.{type(docstring_deprecated_0).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert docstring_deprecated_0.args == [
        "um!lt3J-Yo9JH\t+`",
        "um!lt3J-Yo9JH\t+`",
        "um!lt3J-Yo9JH\t+`",
        "um!lt3J-Yo9JH\t+`",
    ]
    assert docstring_deprecated_0.description == "um!lt3J-Yo9JH\t+`"
    assert docstring_deprecated_0.version == "um!lt3J-Yo9JH\t+`"
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "key",
        "param",
        "parameter",
        "arg",
        "argument",
        "attribute",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "exception", "except", "raise"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}


def test_case_2():
    str_0 = 'i"E#'
    str_1 = "3@q2E.y{QW)^=\x0bk%^x"
    str_2 = "f\nQ6}P"
    list_0 = [str_0, str_1, str_2]
    none_type_0 = None
    docstring_param_0 = module_0.DocstringParam(
        list_0, str_2, str_0, none_type_0, none_type_0, str_1
    )
    assert (
        f"{type(docstring_param_0).__module__}.{type(docstring_param_0).__qualname__}"
        == "common.DocstringParam"
    )
    assert docstring_param_0.args == ['i"E#', "3@q2E.y{QW)^=\x0bk%^x", "f\nQ6}P"]
    assert docstring_param_0.description == "f\nQ6}P"
    assert docstring_param_0.arg_name == 'i"E#'
    assert docstring_param_0.type_name is None
    assert docstring_param_0.is_optional is None
    assert docstring_param_0.default == "3@q2E.y{QW)^=\x0bk%^x"
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "key",
        "param",
        "parameter",
        "arg",
        "argument",
        "attribute",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "exception", "except", "raise"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}


def test_case_3():
    str_0 = "\r"
    list_0 = [str_0]
    bool_0 = True
    docstring_returns_0 = module_0.DocstringReturns(list_0, str_0, str_0, bool_0)
    assert (
        f"{type(docstring_returns_0).__module__}.{type(docstring_returns_0).__qualname__}"
        == "common.DocstringReturns"
    )
    assert docstring_returns_0.args == ["\r"]
    assert docstring_returns_0.description == "\r"
    assert docstring_returns_0.type_name == "\r"
    assert docstring_returns_0.is_generator is True
    assert docstring_returns_0.return_name is None
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "key",
        "param",
        "parameter",
        "arg",
        "argument",
        "attribute",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "exception", "except", "raise"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}


def test_case_4():
    str_0 = 'x"x|E^6:'
    list_0 = [str_0]
    docstring_raises_0 = module_0.DocstringRaises(list_0, list_0, str_0)
    assert (
        f"{type(docstring_raises_0).__module__}.{type(docstring_raises_0).__qualname__}"
        == "common.DocstringRaises"
    )
    assert docstring_raises_0.args == ['x"x|E^6:']
    assert docstring_raises_0.description == ['x"x|E^6:']
    assert docstring_raises_0.type_name == 'x"x|E^6:'
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "key",
        "param",
        "parameter",
        "arg",
        "argument",
        "attribute",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "exception", "except", "raise"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}


def test_case_5():
    bool_0 = True
    none_type_0 = None
    docstring_deprecated_0 = module_0.DocstringDeprecated(
        bool_0, none_type_0, none_type_0
    )
    assert (
        f"{type(docstring_deprecated_0).__module__}.{type(docstring_deprecated_0).__qualname__}"
        == "common.DocstringDeprecated"
    )
    assert docstring_deprecated_0.args is True
    assert docstring_deprecated_0.description is None
    assert docstring_deprecated_0.version is None
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "key",
        "param",
        "parameter",
        "arg",
        "argument",
        "attribute",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "exception", "except", "raise"}
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    str_0 = "M3L1cFavY3`oXa"
    str_1 = "Sr>i|3\x0csqJoTFi6V;"
    list_0 = [str_0, str_1, str_1]
    docstring_example_0 = module_0.DocstringExample(list_0, str_1, str_1)
    assert (
        f"{type(docstring_example_0).__module__}.{type(docstring_example_0).__qualname__}"
        == "common.DocstringExample"
    )
    assert docstring_example_0.args == [
        "M3L1cFavY3`oXa",
        "Sr>i|3\x0csqJoTFi6V;",
        "Sr>i|3\x0csqJoTFi6V;",
    ]
    assert docstring_example_0.description == "Sr>i|3\x0csqJoTFi6V;"
    assert docstring_example_0.snippet == "Sr>i|3\x0csqJoTFi6V;"


def test_case_6():
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
        "keyword",
        "key",
        "param",
        "parameter",
        "arg",
        "argument",
        "attribute",
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
