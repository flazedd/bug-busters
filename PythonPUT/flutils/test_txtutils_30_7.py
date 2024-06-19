# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import txtutils as module_0
import re as module_1
import enum as module_2


def test_case_0():
    bytes_0 = b"\x1e\xf7p"
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(
        subsequent_indent=bytes_0,
        fix_sentence_endings=bytes_0,
        break_long_words=bytes_0,
    )
    assert (
        f"{type(ansi_text_wrapper_0).__module__}.{type(ansi_text_wrapper_0).__qualname__}"
        == "txtutils.AnsiTextWrapper"
    )
    assert ansi_text_wrapper_0.width == 70
    assert ansi_text_wrapper_0.expand_tabs is True
    assert ansi_text_wrapper_0.replace_whitespace is True
    assert ansi_text_wrapper_0.fix_sentence_endings == b"\x1e\xf7p"
    assert ansi_text_wrapper_0.break_long_words == b"\x1e\xf7p"
    assert ansi_text_wrapper_0.drop_whitespace is True
    assert ansi_text_wrapper_0.break_on_hyphens is True
    assert ansi_text_wrapper_0.tabsize == 8
    assert ansi_text_wrapper_0.max_lines is None
    assert module_0.hexversion == 50987248
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent).__module__}.{type(module_0.AnsiTextWrapper.initial_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.initial_indent_len.attrname == "initial_indent_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert (
        module_0.AnsiTextWrapper.subsequent_indent_len.attrname
        == "subsequent_indent_len"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder).__module__}.{type(module_0.AnsiTextWrapper.placeholder).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.placeholder_len.attrname == "placeholder_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len.lock).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len.lock).__qualname__}"
        == "_thread.RLock"
    )


def test_case_1():
    str_0 = "C+Yj#fBh"
    int_0 = module_0.len_without_ansi(str_0)
    assert int_0 == 8
    assert module_0.hexversion == 50987248


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x1e\xf7p"
    module_0.len_without_ansi(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    module_0.len_without_ansi(bool_0)


def test_case_4():
    bytes_0 = b"\x1e\xf7p"
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(
        subsequent_indent=bytes_0,
        fix_sentence_endings=bytes_0,
        break_long_words=bytes_0,
    )
    assert (
        f"{type(ansi_text_wrapper_0).__module__}.{type(ansi_text_wrapper_0).__qualname__}"
        == "txtutils.AnsiTextWrapper"
    )
    assert ansi_text_wrapper_0.width == 70
    assert ansi_text_wrapper_0.expand_tabs is True
    assert ansi_text_wrapper_0.replace_whitespace is True
    assert ansi_text_wrapper_0.fix_sentence_endings == b"\x1e\xf7p"
    assert ansi_text_wrapper_0.break_long_words == b"\x1e\xf7p"
    assert ansi_text_wrapper_0.drop_whitespace is True
    assert ansi_text_wrapper_0.break_on_hyphens is True
    assert ansi_text_wrapper_0.tabsize == 8
    assert ansi_text_wrapper_0.max_lines is None
    assert module_0.hexversion == 50987248
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent).__module__}.{type(module_0.AnsiTextWrapper.initial_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.initial_indent_len.attrname == "initial_indent_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert (
        module_0.AnsiTextWrapper.subsequent_indent_len.attrname
        == "subsequent_indent_len"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder).__module__}.{type(module_0.AnsiTextWrapper.placeholder).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.placeholder_len.attrname == "placeholder_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len.lock).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    str_0 = "b\tZs6{uW<k#\t,s]~n4"
    list_0 = ansi_text_wrapper_0.wrap(str_0)


def test_case_5():
    bool_0 = False
    none_type_0 = None
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(
        subsequent_indent=none_type_0, expand_tabs=none_type_0, max_lines=bool_0
    )
    assert (
        f"{type(ansi_text_wrapper_0).__module__}.{type(ansi_text_wrapper_0).__qualname__}"
        == "txtutils.AnsiTextWrapper"
    )
    assert ansi_text_wrapper_0.width == 70
    assert ansi_text_wrapper_0.expand_tabs is None
    assert ansi_text_wrapper_0.replace_whitespace is True
    assert ansi_text_wrapper_0.fix_sentence_endings is False
    assert ansi_text_wrapper_0.break_long_words is True
    assert ansi_text_wrapper_0.drop_whitespace is True
    assert ansi_text_wrapper_0.break_on_hyphens is True
    assert ansi_text_wrapper_0.tabsize == 8
    assert ansi_text_wrapper_0.max_lines is False
    assert module_0.hexversion == 50987248
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent).__module__}.{type(module_0.AnsiTextWrapper.initial_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.initial_indent_len.attrname == "initial_indent_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert (
        module_0.AnsiTextWrapper.subsequent_indent_len.attrname
        == "subsequent_indent_len"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder).__module__}.{type(module_0.AnsiTextWrapper.placeholder).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.placeholder_len.attrname == "placeholder_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len.lock).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    str_0 = "[Y"
    str_1 = ansi_text_wrapper_0.fill(str_0)
    assert str_1 == "[Y"


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    none_type_0 = None
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(
        subsequent_indent=none_type_0, expand_tabs=none_type_0, max_lines=bool_0
    )
    assert (
        f"{type(ansi_text_wrapper_0).__module__}.{type(ansi_text_wrapper_0).__qualname__}"
        == "txtutils.AnsiTextWrapper"
    )
    assert ansi_text_wrapper_0.width == 70
    assert ansi_text_wrapper_0.expand_tabs is None
    assert ansi_text_wrapper_0.replace_whitespace is True
    assert ansi_text_wrapper_0.fix_sentence_endings is False
    assert ansi_text_wrapper_0.break_long_words is True
    assert ansi_text_wrapper_0.drop_whitespace is True
    assert ansi_text_wrapper_0.break_on_hyphens is True
    assert ansi_text_wrapper_0.tabsize == 8
    assert ansi_text_wrapper_0.max_lines is False
    assert module_0.hexversion == 50987248
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent).__module__}.{type(module_0.AnsiTextWrapper.initial_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.initial_indent_len.attrname == "initial_indent_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert (
        module_0.AnsiTextWrapper.subsequent_indent_len.attrname
        == "subsequent_indent_len"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder).__module__}.{type(module_0.AnsiTextWrapper.placeholder).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.placeholder_len.attrname == "placeholder_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len.lock).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    str_0 = "\r"
    str_1 = ansi_text_wrapper_0.fill(str_0)
    assert str_1 == ""
    module_0.len_without_ansi(ansi_text_wrapper_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = ""
    str_1 = "Convert the given ``text`` of base64 characters into the base64\n    decoded bytes.\n\n    Args:\n        text (str): The string input.  The given string input can span\n            across many lines and be indented any number of spaces.\n        errors (str): Not used.  This argument exists to meet the\n            interface requirements.  Any value given to this argument\n            is ignored.\n\n    Returns:\n        bytes: The given ``text`` converted into base64 bytes.\n        int: The length of the returned bytes.\n    "
    list_0 = [str_0, str_1, str_1]
    int_0 = module_0.len_without_ansi(str_0)
    assert int_0 == 0
    assert module_0.hexversion == 50987248
    int_1 = module_0.len_without_ansi(list_0)
    assert int_1 == 1042
    int_2 = module_0.len_without_ansi(str_0)
    assert int_2 == 0
    bytes_0 = b"\\\xb6n\x8eGf\xb6\x13\xe9\x12"
    none_type_0 = None
    module_1.findall(bytes_0, none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    bool_0 = False
    none_type_0 = None
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(
        subsequent_indent=none_type_0, expand_tabs=none_type_0, max_lines=bool_0
    )
    assert (
        f"{type(ansi_text_wrapper_0).__module__}.{type(ansi_text_wrapper_0).__qualname__}"
        == "txtutils.AnsiTextWrapper"
    )
    assert ansi_text_wrapper_0.width == 70
    assert ansi_text_wrapper_0.expand_tabs is None
    assert ansi_text_wrapper_0.replace_whitespace is True
    assert ansi_text_wrapper_0.fix_sentence_endings is False
    assert ansi_text_wrapper_0.break_long_words is True
    assert ansi_text_wrapper_0.drop_whitespace is True
    assert ansi_text_wrapper_0.break_on_hyphens is True
    assert ansi_text_wrapper_0.tabsize == 8
    assert ansi_text_wrapper_0.max_lines is False
    assert module_0.hexversion == 50987248
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent).__module__}.{type(module_0.AnsiTextWrapper.initial_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.initial_indent_len.attrname == "initial_indent_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert (
        module_0.AnsiTextWrapper.subsequent_indent_len.attrname
        == "subsequent_indent_len"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder).__module__}.{type(module_0.AnsiTextWrapper.placeholder).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.placeholder_len.attrname == "placeholder_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len.lock).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    str_0 = ""
    str_1 = "8@pYt^l~LO<SP'[#7"
    str_2 = ansi_text_wrapper_0.fill(str_1)
    assert str_2 == "8@pYt^l~LO<SP'[#7"
    str_3 = ansi_text_wrapper_0.fill(str_0)
    assert str_3 == ""
    module_0.len_without_ansi(ansi_text_wrapper_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "tULTdCk3},"
    float_0 = -251.271
    str_1 = "0F-t)"
    bool_0 = True
    bool_1 = True
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(
        float_0,
        subsequent_indent=str_1,
        break_long_words=bool_0,
        drop_whitespace=bool_1,
        break_on_hyphens=bool_1,
    )
    assert (
        f"{type(ansi_text_wrapper_0).__module__}.{type(ansi_text_wrapper_0).__qualname__}"
        == "txtutils.AnsiTextWrapper"
    )
    assert ansi_text_wrapper_0.width == pytest.approx(-251.271, abs=0.01, rel=0.01)
    assert ansi_text_wrapper_0.expand_tabs is True
    assert ansi_text_wrapper_0.replace_whitespace is True
    assert ansi_text_wrapper_0.fix_sentence_endings is False
    assert ansi_text_wrapper_0.break_long_words is True
    assert ansi_text_wrapper_0.drop_whitespace is True
    assert ansi_text_wrapper_0.break_on_hyphens is True
    assert ansi_text_wrapper_0.tabsize == 8
    assert ansi_text_wrapper_0.max_lines is None
    assert module_0.hexversion == 50987248
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent).__module__}.{type(module_0.AnsiTextWrapper.initial_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.initial_indent_len.attrname == "initial_indent_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert (
        module_0.AnsiTextWrapper.subsequent_indent_len.attrname
        == "subsequent_indent_len"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder).__module__}.{type(module_0.AnsiTextWrapper.placeholder).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.placeholder_len.attrname == "placeholder_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len.lock).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    ansi_text_wrapper_0.fill(str_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    bool_0 = True
    none_type_0 = None
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(
        subsequent_indent=none_type_0, expand_tabs=none_type_0, max_lines=bool_0
    )
    assert (
        f"{type(ansi_text_wrapper_0).__module__}.{type(ansi_text_wrapper_0).__qualname__}"
        == "txtutils.AnsiTextWrapper"
    )
    assert ansi_text_wrapper_0.width == 70
    assert ansi_text_wrapper_0.expand_tabs is None
    assert ansi_text_wrapper_0.replace_whitespace is True
    assert ansi_text_wrapper_0.fix_sentence_endings is False
    assert ansi_text_wrapper_0.break_long_words is True
    assert ansi_text_wrapper_0.drop_whitespace is True
    assert ansi_text_wrapper_0.break_on_hyphens is True
    assert ansi_text_wrapper_0.tabsize == 8
    assert ansi_text_wrapper_0.max_lines is True
    assert module_0.hexversion == 50987248
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent).__module__}.{type(module_0.AnsiTextWrapper.initial_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.initial_indent_len.attrname == "initial_indent_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert (
        module_0.AnsiTextWrapper.subsequent_indent_len.attrname
        == "subsequent_indent_len"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder).__module__}.{type(module_0.AnsiTextWrapper.placeholder).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.placeholder_len.attrname == "placeholder_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len.lock).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    str_0 = "\r"
    str_1 = 'gsQQ^"A'
    ansi_text_wrapper_1 = module_0.AnsiTextWrapper(
        subsequent_indent=none_type_0,
        replace_whitespace=bool_0,
        drop_whitespace=none_type_0,
        placeholder=str_1,
    )
    assert (
        f"{type(ansi_text_wrapper_1).__module__}.{type(ansi_text_wrapper_1).__qualname__}"
        == "txtutils.AnsiTextWrapper"
    )
    assert ansi_text_wrapper_1.width == 70
    assert ansi_text_wrapper_1.expand_tabs is True
    assert ansi_text_wrapper_1.replace_whitespace is True
    assert ansi_text_wrapper_1.fix_sentence_endings is False
    assert ansi_text_wrapper_1.break_long_words is True
    assert ansi_text_wrapper_1.drop_whitespace is None
    assert ansi_text_wrapper_1.break_on_hyphens is True
    assert ansi_text_wrapper_1.tabsize == 8
    assert ansi_text_wrapper_1.max_lines is None
    list_0 = ansi_text_wrapper_1.wrap(str_0)
    ansi_text_wrapper_0.fill(none_type_0)


def test_case_11():
    none_type_0 = None
    str_0 = "!B`M"
    dict_0 = {str_0: str_0, str_0: none_type_0, str_0: none_type_0, str_0: none_type_0}
    str_1 = "tULTdCk3},"
    str_2 = "0F-t)"
    bool_0 = True
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(
        bool_0,
        subsequent_indent=str_2,
        break_long_words=str_1,
        drop_whitespace=bool_0,
        break_on_hyphens=bool_0,
    )
    assert (
        f"{type(ansi_text_wrapper_0).__module__}.{type(ansi_text_wrapper_0).__qualname__}"
        == "txtutils.AnsiTextWrapper"
    )
    assert ansi_text_wrapper_0.width is True
    assert ansi_text_wrapper_0.expand_tabs is True
    assert ansi_text_wrapper_0.replace_whitespace is True
    assert ansi_text_wrapper_0.fix_sentence_endings is False
    assert ansi_text_wrapper_0.break_long_words == "tULTdCk3},"
    assert ansi_text_wrapper_0.drop_whitespace is True
    assert ansi_text_wrapper_0.break_on_hyphens is True
    assert ansi_text_wrapper_0.tabsize == 8
    assert ansi_text_wrapper_0.max_lines is None
    assert module_0.hexversion == 50987248
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent).__module__}.{type(module_0.AnsiTextWrapper.initial_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.initial_indent_len.attrname == "initial_indent_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert (
        module_0.AnsiTextWrapper.subsequent_indent_len.attrname
        == "subsequent_indent_len"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder).__module__}.{type(module_0.AnsiTextWrapper.placeholder).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.placeholder_len.attrname == "placeholder_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len.lock).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    var_0 = ansi_text_wrapper_0.fill(str_1)
    assert (
        var_0
        == "t\n0F-t)U\n0F-t)L\n0F-t)T\n0F-t)d\n0F-t)C\n0F-t)k\n0F-t)3\n0F-t)}\n0F-t),"
    )
    with pytest.raises(TypeError):
        var_0.__new__(none_type_0, none_type_0, none_type_0, none_type_0, **dict_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    bool_0 = True
    str_0 = "Convert the given ``text`` of base64 characters into the base64\n    decoded bytes.\n\n    Args:\n        text (str): The string input.  The given string input can span\n            across many lines and be indented any number of spaces.\n        errors (str): Not used.  This argument exists to meet the\n            interface requirements.  Any value given to this argument\n            is ignored.\n\n    Returns:\n        bytes: The given ``text`` converted into base64 bytes.\n        int: The length of the returned bytes.\n    "
    enum_dict_0 = module_2._EnumDict()
    assert (
        f"{type(enum_dict_0).__module__}.{type(enum_dict_0).__qualname__}"
        == "enum._EnumDict"
    )
    assert len(enum_dict_0) == 0
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(
        subsequent_indent=enum_dict_0, expand_tabs=enum_dict_0, max_lines=bool_0
    )
    assert (
        f"{type(ansi_text_wrapper_0).__module__}.{type(ansi_text_wrapper_0).__qualname__}"
        == "txtutils.AnsiTextWrapper"
    )
    assert ansi_text_wrapper_0.width == 70
    assert (
        f"{type(ansi_text_wrapper_0.expand_tabs).__module__}.{type(ansi_text_wrapper_0.expand_tabs).__qualname__}"
        == "enum._EnumDict"
    )
    assert len(ansi_text_wrapper_0.expand_tabs) == 0
    assert ansi_text_wrapper_0.replace_whitespace is True
    assert ansi_text_wrapper_0.fix_sentence_endings is False
    assert ansi_text_wrapper_0.break_long_words is True
    assert ansi_text_wrapper_0.drop_whitespace is True
    assert ansi_text_wrapper_0.break_on_hyphens is True
    assert ansi_text_wrapper_0.tabsize == 8
    assert ansi_text_wrapper_0.max_lines is True
    assert module_0.hexversion == 50987248
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent).__module__}.{type(module_0.AnsiTextWrapper.initial_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.initial_indent_len.attrname == "initial_indent_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert (
        module_0.AnsiTextWrapper.subsequent_indent_len.attrname
        == "subsequent_indent_len"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder).__module__}.{type(module_0.AnsiTextWrapper.placeholder).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.placeholder_len.attrname == "placeholder_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len.lock).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    list_0 = ansi_text_wrapper_0.wrap(str_0)
    assert ansi_text_wrapper_0.placeholder_len == 6
    int_0 = module_0.len_without_ansi(enum_dict_0)
    assert int_0 == 0
    str_1 = ansi_text_wrapper_0.fill(str_0)
    assert (
        str_1 == "Convert the given ``text`` of base64 characters into the base64 [...]"
    )
    list_1 = []
    module_1.match(bool_0, bool_0, list_1)


@pytest.mark.xfail(strict=True)
def test_case_13():
    bool_0 = True
    str_0 = "CwH~.(273v'ldt>.U,"
    str_1 = "Convert the given ``text`` of base64 characters into the base64\n    decoded bytes.\n\n    Args:\n        text (str): The string input.  The given string input can span\n            across many lines and be indented any number of spaces.\n        errors (str): Not used.  This argument exists to meet the\n            interface requirements.  Any value given to this argument\n            is ignored.\n\n    Returns:\n        bytes: The given ``text`` converted into base64 bytes.\n        int: The length of the returned bytes.\n    "
    enum_dict_0 = module_2._EnumDict()
    assert (
        f"{type(enum_dict_0).__module__}.{type(enum_dict_0).__qualname__}"
        == "enum._EnumDict"
    )
    assert len(enum_dict_0) == 0
    ansi_text_wrapper_0 = module_0.AnsiTextWrapper(
        subsequent_indent=enum_dict_0,
        expand_tabs=enum_dict_0,
        max_lines=bool_0,
        placeholder=str_1,
    )
    assert (
        f"{type(ansi_text_wrapper_0).__module__}.{type(ansi_text_wrapper_0).__qualname__}"
        == "txtutils.AnsiTextWrapper"
    )
    assert ansi_text_wrapper_0.width == 70
    assert (
        f"{type(ansi_text_wrapper_0.expand_tabs).__module__}.{type(ansi_text_wrapper_0.expand_tabs).__qualname__}"
        == "enum._EnumDict"
    )
    assert len(ansi_text_wrapper_0.expand_tabs) == 0
    assert ansi_text_wrapper_0.replace_whitespace is True
    assert ansi_text_wrapper_0.fix_sentence_endings is False
    assert ansi_text_wrapper_0.break_long_words is True
    assert ansi_text_wrapper_0.drop_whitespace is True
    assert ansi_text_wrapper_0.break_on_hyphens is True
    assert ansi_text_wrapper_0.tabsize == 8
    assert ansi_text_wrapper_0.max_lines is True
    assert module_0.hexversion == 50987248
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent).__module__}.{type(module_0.AnsiTextWrapper.initial_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.initial_indent_len.attrname == "initial_indent_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.initial_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len).__qualname__}"
        == "functools.cached_property"
    )
    assert (
        module_0.AnsiTextWrapper.subsequent_indent_len.attrname
        == "subsequent_indent_len"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__module__}.{type(module_0.AnsiTextWrapper.subsequent_indent_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder).__module__}.{type(module_0.AnsiTextWrapper.placeholder).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.AnsiTextWrapper.placeholder_len.attrname == "placeholder_len"
    assert (
        f"{type(module_0.AnsiTextWrapper.placeholder_len.lock).__module__}.{type(module_0.AnsiTextWrapper.placeholder_len.lock).__qualname__}"
        == "_thread.RLock"
    )
    ansi_text_wrapper_0.wrap(str_0)
