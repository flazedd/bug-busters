# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import google as module_0
import common as module_1
import inspect as module_2
import tokenize as module_3


def test_case_0():
    str_0 = "I e"
    google_parser_0 = module_0.GoogleParser(str_0, str_0)
    assert (
        f"{type(google_parser_0).__module__}.{type(google_parser_0).__qualname__}"
        == "google.GoogleParser"
    )
    assert (
        f"{type(google_parser_0.sections).__module__}.{type(google_parser_0.sections).__qualname__}"
        == "builtins.dict"
    )
    assert len(google_parser_0.sections) == 3
    assert google_parser_0.title_colon == "I e"
    assert (
        f"{type(google_parser_0.titles_re).__module__}.{type(google_parser_0.titles_re).__qualname__}"
        == "re.Pattern"
    )
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    assert module_0.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert (
        f"{type(module_0.GOOGLE_TYPED_ARG_REGEX).__module__}.{type(module_0.GOOGLE_TYPED_ARG_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.GOOGLE_ARG_DESC_REGEX).__module__}.{type(module_0.GOOGLE_ARG_DESC_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.MULTIPLE_PATTERN).__module__}.{type(module_0.MULTIPLE_PATTERN).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 12
    google_parser_1 = module_0.GoogleParser()
    assert (
        f"{type(google_parser_1).__module__}.{type(google_parser_1).__qualname__}"
        == "google.GoogleParser"
    )
    assert (
        f"{type(google_parser_1.sections).__module__}.{type(google_parser_1.sections).__qualname__}"
        == "builtins.dict"
    )
    assert len(google_parser_1.sections) == 12
    assert google_parser_1.title_colon is True
    assert (
        f"{type(google_parser_1.titles_re).__module__}.{type(google_parser_1.titles_re).__qualname__}"
        == "re.Pattern"
    )
    str_1 = ""
    docstring_0 = google_parser_1.parse(str_1)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description is None
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.GOOGLE
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )
    none_type_0 = None
    with pytest.raises(TypeError):
        module_2.getgeneratorlocals(none_type_0)


def test_case_1():
    none_type_0 = None
    google_parser_0 = module_0.GoogleParser(title_colon=none_type_0)
    assert (
        f"{type(google_parser_0).__module__}.{type(google_parser_0).__qualname__}"
        == "google.GoogleParser"
    )
    assert (
        f"{type(google_parser_0.sections).__module__}.{type(google_parser_0.sections).__qualname__}"
        == "builtins.dict"
    )
    assert len(google_parser_0.sections) == 12
    assert google_parser_0.title_colon is None
    assert (
        f"{type(google_parser_0.titles_re).__module__}.{type(google_parser_0.titles_re).__qualname__}"
        == "re.Pattern"
    )
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    assert module_0.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert (
        f"{type(module_0.GOOGLE_TYPED_ARG_REGEX).__module__}.{type(module_0.GOOGLE_TYPED_ARG_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.GOOGLE_ARG_DESC_REGEX).__module__}.{type(module_0.GOOGLE_ARG_DESC_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.MULTIPLE_PATTERN).__module__}.{type(module_0.MULTIPLE_PATTERN).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 12


def test_case_2():
    str_0 = "DHE@5d1By_`gPA)%)Ct"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "DHE@5d1By_`gPA)%)Ct"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.GOOGLE
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    assert module_0.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert (
        f"{type(module_0.GOOGLE_TYPED_ARG_REGEX).__module__}.{type(module_0.GOOGLE_TYPED_ARG_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.GOOGLE_ARG_DESC_REGEX).__module__}.{type(module_0.GOOGLE_ARG_DESC_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.MULTIPLE_PATTERN).__module__}.{type(module_0.MULTIPLE_PATTERN).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 12
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )


def test_case_3():
    none_type_0 = None
    docstring_0 = module_0.parse(none_type_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description is None
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.GOOGLE
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    assert module_0.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert (
        f"{type(module_0.GOOGLE_TYPED_ARG_REGEX).__module__}.{type(module_0.GOOGLE_TYPED_ARG_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.GOOGLE_ARG_DESC_REGEX).__module__}.{type(module_0.GOOGLE_ARG_DESC_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.MULTIPLE_PATTERN).__module__}.{type(module_0.MULTIPLE_PATTERN).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 12
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )


@pytest.mark.xfail(strict=True)
def test_case_4():
    module_0.Section()


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    google_parser_0 = module_0.GoogleParser(none_type_0)
    assert (
        f"{type(google_parser_0).__module__}.{type(google_parser_0).__qualname__}"
        == "google.GoogleParser"
    )
    assert (
        f"{type(google_parser_0.sections).__module__}.{type(google_parser_0.sections).__qualname__}"
        == "builtins.dict"
    )
    assert len(google_parser_0.sections) == 12
    assert google_parser_0.title_colon is True
    assert (
        f"{type(google_parser_0.titles_re).__module__}.{type(google_parser_0.titles_re).__qualname__}"
        == "re.Pattern"
    )
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    assert module_0.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert (
        f"{type(module_0.GOOGLE_TYPED_ARG_REGEX).__module__}.{type(module_0.GOOGLE_TYPED_ARG_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.GOOGLE_ARG_DESC_REGEX).__module__}.{type(module_0.GOOGLE_ARG_DESC_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.MULTIPLE_PATTERN).__module__}.{type(module_0.MULTIPLE_PATTERN).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 12
    google_parser_0.add_section(none_type_0)


def test_case_6():
    str_0 = "rOyf<\n}+r3FG\rO/TV"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "rOyf<"
    assert docstring_0.long_description == "}+r3FG\rO/TV"
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.GOOGLE
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    assert module_0.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert (
        f"{type(module_0.GOOGLE_TYPED_ARG_REGEX).__module__}.{type(module_0.GOOGLE_TYPED_ARG_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.GOOGLE_ARG_DESC_REGEX).__module__}.{type(module_0.GOOGLE_ARG_DESC_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.MULTIPLE_PATTERN).__module__}.{type(module_0.MULTIPLE_PATTERN).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 12
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )


def test_case_7():
    str_0 = "DHE@5d1By_`gPA)%)Ct"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "DHE@5d1By_`gPA)%)Ct"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.GOOGLE
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    assert module_0.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert (
        f"{type(module_0.GOOGLE_TYPED_ARG_REGEX).__module__}.{type(module_0.GOOGLE_TYPED_ARG_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.GOOGLE_ARG_DESC_REGEX).__module__}.{type(module_0.GOOGLE_ARG_DESC_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.MULTIPLE_PATTERN).__module__}.{type(module_0.MULTIPLE_PATTERN).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 12
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )
    str_1 = module_0.compose(docstring_0)
    assert str_1 == "DHE@5d1By_`gPA)%)Ct"
    assert module_1.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_1.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"examples", "example"}


def test_case_8():
    str_0 = "rOyf<\n}+r3FG\rO/TV"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "rOyf<"
    assert docstring_0.long_description == "}+r3FG\rO/TV"
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.GOOGLE
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    assert module_0.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert (
        f"{type(module_0.GOOGLE_TYPED_ARG_REGEX).__module__}.{type(module_0.GOOGLE_TYPED_ARG_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.GOOGLE_ARG_DESC_REGEX).__module__}.{type(module_0.GOOGLE_ARG_DESC_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.MULTIPLE_PATTERN).__module__}.{type(module_0.MULTIPLE_PATTERN).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 12
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )
    str_1 = module_0.compose(docstring_0, indent=str_0)
    assert str_1 == "rOyf<\n}+r3FG\rO/TV"
    assert module_1.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_1.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"examples", "example"}


@pytest.mark.xfail(strict=True)
def test_case_9():
    section_type_0 = module_0.SectionType.SINGULAR
    str_0 = "Ab\ts_|>k\nL\x0cnl%"
    str_1 = "+"
    docstring_0 = module_0.parse(str_1)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "+"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.GOOGLE
    assert module_0.EXAMPLES_KEYWORDS == {"examples", "example"}
    assert module_0.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_0.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_0.YIELDS_KEYWORDS == {"yields", "yield"}
    assert (
        f"{type(module_0.GOOGLE_TYPED_ARG_REGEX).__module__}.{type(module_0.GOOGLE_TYPED_ARG_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.GOOGLE_ARG_DESC_REGEX).__module__}.{type(module_0.GOOGLE_ARG_DESC_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.MULTIPLE_PATTERN).__module__}.{type(module_0.MULTIPLE_PATTERN).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 12
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )
    docstring_1 = module_0.parse(str_0)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description == "Ab      s_|>k"
    assert docstring_1.long_description == "L\x0cnl%"
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.GOOGLE
    assert module_1.PARAM_KEYWORDS == {
        "attribute",
        "param",
        "parameter",
        "arg",
        "key",
        "keyword",
        "argument",
    }
    assert module_1.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"examples", "example"}
    docstring_2 = module_0.parse(section_type_0)
    assert (
        f"{type(docstring_2).__module__}.{type(docstring_2).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_2.short_description is None
    assert docstring_2.long_description is None
    assert docstring_2.blank_after_short_description is False
    assert docstring_2.blank_after_long_description is False
    assert docstring_2.meta == []
    assert docstring_2.style == module_1.DocstringStyle.GOOGLE
    str_2 = module_0.compose(docstring_2, indent=docstring_0)
    assert str_2 == ""
    module_3.untokenize(str_0)