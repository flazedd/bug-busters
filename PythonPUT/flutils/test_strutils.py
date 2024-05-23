# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import strutils as module_0
import re as module_1


def test_case_0():
    str_0 = "eutf8h"
    str_1 = module_0.as_escaped_unicode_literal(str_0)
    assert str_1 == "\\x65\\x75\\x74\\x66\\x38\\x68"


def test_case_1():
    str_0 = "utf-8"
    str_1 = module_0.as_escaped_utf8_literal(str_0)
    assert str_1 == "\\x75\\x74\\x66\\x2d\\x38"
    str_2 = module_0.underscore_to_camel(str_0)
    assert str_2 == "utf-8"


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "eutf8h"
    bool_0 = False
    str_1 = module_0.underscore_to_camel(str_0, bool_0)
    assert str_1 == "Eutf8h"
    str_2 = module_0.as_escaped_utf8_literal(str_1)
    assert str_2 == "\\x45\\x75\\x74\\x66\\x38\\x68"
    str_3 = "G tO0ek"
    str_4 = module_0.camel_to_underscore(str_2)
    assert str_4 == "\\x45\\x75\\x74\\x66\\x38\\x68"
    str_5 = module_0.convert_escaped_unicode_literal(str_4)
    assert str_5 == "Eutf8h"
    str_6 = module_0.as_escaped_unicode_literal(str_3)
    assert str_6 == "\\x47\\x20\\x74\\x4f\\x30\\x65\\x6b"
    module_0.convert_escaped_utf8_literal(str_5)


def test_case_3():
    str_0 = "?HEeV4S(j*"
    str_1 = module_0.convert_escaped_unicode_literal(str_0)
    assert str_1 == "?HEeV4S(j*"


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    module_0.camel_to_underscore(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "CN:+R]Z[/+ju(Ba:('pX"
    module_0.convert_escaped_utf8_literal(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "d\\M]1t Y;ZSbC<"
    str_1 = module_0.as_escaped_utf8_literal(str_0)
    assert (
        str_1
        == "\\x64\\x5c\\x4d\\x5d\\x31\\x74\\x20\\x59\\x3b\\x5a\\x53\\x62\\x43\\x3c"
    )
    str_2 = "Convert a :obj:`str`, that may contain escaped utf8 hexadecimal, to\n    bytes of escaped utf8 hexadecimal.\n\n    Args:\n        text (str or :obj:`~UserString`): The string input.\n        errors (str or :obj:`~UserString`): The error checking level.\n\n    Returns:\n        bytes: The given ``text`` converted into escaped utf8 bytes.\n        int: The number of given ``text`` characters consumed\n\n    Raises:\n         UnicodeEncodeError: if the given ``text`` contains escaped\n            utf8 hexadecimal that references invalid utf8 bytes.\n    "
    str_3 = module_0.convert_escaped_unicode_literal(str_2)
    assert (
        str_3
        == "Convert a :obj:`str`, that may contain escaped utf8 hexadecimal, to\n    bytes of escaped utf8 hexadecimal.\n\n    Args:\n        text (str or :obj:`~UserString`): The string input.\n        errors (str or :obj:`~UserString`): The error checking level.\n\n    Returns:\n        bytes: The given ``text`` converted into escaped utf8 bytes.\n        int: The number of given ``text`` characters consumed\n\n    Raises:\n         UnicodeEncodeError: if the given ``text`` contains escaped\n            utf8 hexadecimal that references invalid utf8 bytes.\n    "
    )
    str_4 = "$hWT9e13-+M+'vrkk"
    str_5 = module_0.camel_to_underscore(str_1)
    assert (
        str_5
        == "\\x64\\x5c\\x4d\\x5d\\x31\\x74\\x20\\x59\\x3b\\x5a\\x53\\x62\\x43\\x3c"
    )
    str_6 = ""
    str_7 = module_0.underscore_to_camel(str_6)
    assert str_7 == ""
    str_8 = module_0.as_escaped_utf8_literal(str_4)
    assert (
        str_8
        == "\\x24\\x68\\x57\\x54\\x39\\x65\\x31\\x33\\x2d\\x2b\\x4d\\x2b\\x27\\x76\\x72\\x6b\\x6b"
    )
    none_type_0 = None
    str_9 = module_0.underscore_to_camel(str_8, none_type_0)
    assert (
        str_9
        == "\\x24\\x68\\x57\\x54\\x39\\x65\\x31\\x33\\x2d\\x2b\\x4d\\x2b\\x27\\x76\\x72\\x6b\\x6b"
    )
    str_10 = module_1.purge()
    assert module_1.ASCII == module_1.RegexFlag.ASCII
    assert module_1.A == module_1.RegexFlag.ASCII
    assert module_1.IGNORECASE == module_1.RegexFlag.IGNORECASE
    assert module_1.I == module_1.RegexFlag.IGNORECASE
    assert module_1.LOCALE == module_1.RegexFlag.LOCALE
    assert module_1.L == module_1.RegexFlag.LOCALE
    assert module_1.UNICODE == module_1.RegexFlag.UNICODE
    assert module_1.U == module_1.RegexFlag.UNICODE
    assert module_1.MULTILINE == module_1.RegexFlag.MULTILINE
    assert module_1.M == module_1.RegexFlag.MULTILINE
    assert module_1.DOTALL == module_1.RegexFlag.DOTALL
    assert module_1.S == module_1.RegexFlag.DOTALL
    assert module_1.VERBOSE == module_1.RegexFlag.VERBOSE
    assert module_1.X == module_1.RegexFlag.VERBOSE
    assert module_1.TEMPLATE == module_1.RegexFlag.TEMPLATE
    assert module_1.T == module_1.RegexFlag.TEMPLATE
    assert module_1.DEBUG == module_1.RegexFlag.DEBUG
    module_0.as_escaped_unicode_literal(str_10)
