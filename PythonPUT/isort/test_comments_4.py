# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import comments as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = 'q;[p{< <k|[1R;"o|P$p'
    list_0 = [str_0]
    str_1 = module_0.add_to_line(list_0)
    assert str_1 == ' q;[p{< <k|[1R;"o|P$p'
    str_2 = "a}[2Vv"
    tuple_0 = module_0.parse(str_2)
    none_type_0 = None
    str_3 = module_0.add_to_line(none_type_0)
    assert str_3 == ""
    bytes_0 = b"d\x92\xb0\xc4\x00\x10\xc1,\x7f\x03"
    str_4 = "#("
    tuple_1 = module_0.parse(str_4)
    module_0.parse(bytes_0)


def test_case_1():
    str_0 = "Y\\.%dy>&!KAeTmb}"
    tuple_0 = module_0.parse(str_0)


def test_case_2():
    str_0 = "i2M"
    tuple_0 = module_0.parse(str_0)
    tuple_1 = module_0.parse(str_0)
    tuple_2 = module_0.parse(str_0)
    none_type_0 = None
    tuple_3 = module_0.parse(str_0)
    str_1 = module_0.add_to_line(none_type_0, str_0, tuple_1)
    assert str_1 == "i2M"


def test_case_3():
    list_0 = []
    bool_0 = False
    str_0 = "=7J S\n>n{y}gb"
    str_1 = module_0.add_to_line(list_0, removed=bool_0, comment_prefix=str_0)
    assert str_1 == ""


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    str_0 = "NsqFg%S`k`Tm~T"
    str_1 = "ip~z"
    list_0 = [str_0, str_1]
    none_type_0 = None
    module_0.add_to_line(list_0, none_type_0, comment_prefix=bool_0)


def test_case_5():
    str_0 = "F\x0bBbgjk'\x0c \\z&\n{J"
    str_1 = "#/WRy`D\r*"
    str_2 = "AIeP<J/0V1"
    str_3 = "(>&+X:;"
    str_4 = "@Gc/\x0b6$sFpyn#0ip"
    str_5 = "e@8g#B]g;~8|LR=_&UK"
    list_0 = [str_2, str_3, str_4, str_5]
    bool_0 = True
    str_6 = module_0.add_to_line(list_0, removed=bool_0, comment_prefix=bool_0)
    assert str_6 == ""
    str_7 = ";S?>JB,\\@Ikf)"
    str_8 = "&Gdb7u`g*>+]^s._B"
    list_1 = [str_8, str_8]
    str_9 = module_0.add_to_line(list_1)
    assert str_9 == " &Gdb7u`g*>+]^s._B"
    list_2 = [str_0, str_0, str_1, str_7]
    str_10 = module_0.add_to_line(list_2, removed=str_1)
    assert str_10 == ""
    str_11 = ".?7-313"
    tuple_0 = module_0.parse(str_11)