# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import comments as module_0


def test_case_0():
    str_0 = "R{8{\nI#^kJBHe\rN5AJIh"
    none_type_0 = None
    str_1 = module_0.add_to_line(none_type_0)
    assert str_1 == ""
    str_2 = 'bqwwLLc7):oZ"~D5&V&'
    str_3 = "M~@9"
    tuple_0 = module_0.parse(str_0)
    tuple_1 = module_0.parse(str_3)
    str_4 = '"@=lt^l@lSPvF.@&'
    list_0 = [str_0, str_0, str_2, str_4]
    bool_0 = True
    str_5 = module_0.add_to_line(list_0, removed=bool_0)
    assert str_5 == ""


def test_case_1():
    str_0 = "y."
    list_0 = []
    str_1 = module_0.add_to_line(list_0, str_0, str_0)
    assert str_1 == "y."
    tuple_0 = module_0.parse(str_0)


def test_case_2():
    list_0 = []
    str_0 = module_0.add_to_line(list_0)
    assert str_0 == ""


def test_case_3():
    str_0 = "[I_QHk"
    str_1 = "dKcj\\"
    list_0 = [str_0, str_1]
    str_2 = "j=b:~60eeS{TCTR"
    str_3 = module_0.add_to_line(list_0, removed=list_0, comment_prefix=str_2)
    assert str_3 == ""
    str_4 = module_0.add_to_line(list_0, str_0, comment_prefix=str_0)
    assert str_4 == "[I_QHk[I_QHk [I_QHk; dKcj\\"


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xcaH\r\xd4\xf1Gq\x9e"
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.add_to_line(list_0)