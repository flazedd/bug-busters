# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import comments as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x9d?\xfbU"
    str_0 = "wG-;H[:8BN7,gQW#"
    module_0.add_to_line(bytes_0, str_0)


def test_case_1():
    str_0 = "D"
    str_1 = "!Y1_O:2L"
    tuple_0 = module_0.parse(str_1)
    str_2 = module_0.add_to_line(str_0, str_0)
    assert str_2 == "D D"
    tuple_1 = module_0.parse(str_1)


def test_case_2():
    none_type_0 = None
    bool_0 = True
    str_0 = "zRuv\t+A"
    tuple_0 = module_0.parse(str_0)
    str_1 = module_0.add_to_line(
        none_type_0, removed=bool_0, comment_prefix=none_type_0
    )
    assert str_1 == ""


def test_case_3():
    bool_0 = False
    str_0 = "@ARF]\x0bB1<U75,!\\oo,wv"
    str_1 = module_0.add_to_line(bool_0, comment_prefix=str_0)
    assert str_1 == ""


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    module_0.parse(bool_0)


def test_case_5():
    str_0 = ""
    str_1 = ""
    list_0 = [str_0, str_1, str_0, str_0]
    str_2 = "N_yv7k0)4Yx\x0bI"
    none_type_0 = None
    str_3 = module_0.add_to_line(list_0, str_2, comment_prefix=none_type_0)
    assert str_3 == "N_yv7k0)4Yx\x0bINone "