# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import comments as module_0


def test_case_0():
    none_type_0 = None
    str_0 = '\tFd#\\UL"4v&,o\n;pX>-'
    tuple_0 = module_0.parse(str_0)
    str_1 = module_0.add_to_line(none_type_0, removed=none_type_0)
    assert str_1 == ""


def test_case_1():
    str_0 = 'P/tE.yw|8("Sr'
    tuple_0 = module_0.parse(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "`8WiE(2||d}\x0cLjl"
    str_1 = "\n\r\x0bCZ%:(&~HF`ho"
    str_2 = "?7}2o9Zx_G[)37\t\x0ba"
    list_0 = [str_0, str_1, str_2]
    str_3 = module_0.add_to_line(list_0, str_2, str_1)
    assert str_3 == "?7}2o9Zx_G[)37\t\x0ba"
    none_type_0 = None
    module_0.parse(none_type_0)


def test_case_3():
    none_type_0 = None
    str_0 = module_0.add_to_line(none_type_0, removed=none_type_0)
    assert str_0 == ""
    tuple_0 = module_0.parse(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -1857.0
    str_0 = "oT\rz4y;-<H\ncLtKZ]K"
    module_0.add_to_line(float_0, comment_prefix=str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "C"
    tuple_0 = module_0.parse(str_0)
    str_1 = module_0.add_to_line(tuple_0)
    assert str_1 == " C; "
    none_type_0 = None
    module_0.add_to_line(str_0, none_type_0, comment_prefix=str_1)


def test_case_6():
    bool_0 = False
    str_0 = "SV6gC@}r, >b0d%Fd"
    str_1 = "(O\n%8\x0c7VxM!7Yh2;8"
    list_0 = [str_0, str_0, str_1]
    str_2 = module_0.add_to_line(list_0)
    assert str_2 == " SV6gC@}r, >b0d%Fd; (O\n%8\x0c7VxM!7Yh2;8"
    str_3 = ": LN]U'n"
    tuple_0 = module_0.parse(str_0)
    str_4 = module_0.add_to_line(bool_0, removed=bool_0, comment_prefix=str_3)
    assert str_4 == ""
