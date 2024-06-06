# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import immutable_list as module_0


def test_case_0():
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    bool_0 = immutable_list_0.__eq__(immutable_list_0)
    assert bool_0 is True
    none_type_0 = None
    bool_1 = immutable_list_0.__eq__(none_type_0)
    assert bool_1 is False
    var_0 = immutable_list_0.__len__()
    assert var_0 == 0


def test_case_1():
    none_type_0 = None
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    immutable_list_1 = immutable_list_0.append(none_type_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0


def test_case_2():
    none_type_0 = None
    none_type_1 = None
    immutable_list_0 = module_0.ImmutableList(none_type_1, none_type_1)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    with pytest.raises(ValueError):
        immutable_list_0.__add__(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2012
    str_0 = "DDD'0wUbF"
    immutable_list_0 = module_0.ImmutableList(is_empty=str_0)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    var_0 = immutable_list_0.__len__()
    assert var_0 == 0
    var_0.filter(int_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    immutable_list_1 = module_0.ImmutableList(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    immutable_list_2 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    var_0 = immutable_list_0.reduce(immutable_list_2, immutable_list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_0) == 0
    bool_0 = immutable_list_1.__eq__(var_0)
    assert bool_0 is False
    int_0 = -1042
    var_1 = immutable_list_0.find(int_0)
    str_0 = immutable_list_1.__str__()
    immutable_list_3 = immutable_list_2.append(immutable_list_2)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1
    immutable_list_4 = immutable_list_0.unshift(bool_0)
    assert (
        f"{type(immutable_list_4).__module__}.{type(immutable_list_4).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_4) == 1
    var_2 = immutable_list_0.find(immutable_list_4)
    var_3 = immutable_list_3.__len__()
    assert var_3 == 1
    immutable_list_5 = immutable_list_3.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_5).__module__}.{type(immutable_list_5).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_5) == 2
    immutable_list_2.find(immutable_list_2)


@pytest.mark.xfail(strict=True)
def test_case_5():
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    var_0 = immutable_list_0.to_list()
    var_0.to_list()


@pytest.mark.xfail(strict=True)
def test_case_6():
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    bool_0 = True
    var_0 = immutable_list_0.append(bool_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_0) == 0
    var_1 = immutable_list_0.find(var_0)
    str_0 = var_0.__str__()
    assert str_0 == "ImmutableList[None, True]"
    immutable_list_0.filter(var_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    list_0 = []
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    immutable_list_1 = immutable_list_0.__add__(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    bool_0 = immutable_list_0.__eq__(immutable_list_0)
    assert bool_0 is True
    immutable_list_0.map(list_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    list_0 = []
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    immutable_list_1 = immutable_list_0.__add__(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    var_0 = immutable_list_0.unshift(list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_0) == 1
    immutable_list_2 = immutable_list_1.__add__(immutable_list_1)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 0
    var_1 = immutable_list_0.find(var_0)
    immutable_list_3 = immutable_list_0.unshift(immutable_list_1)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1
    immutable_list_4 = module_0.ImmutableList(list_0)
    assert (
        f"{type(immutable_list_4).__module__}.{type(immutable_list_4).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_4) == 1
    var_2 = immutable_list_2.reduce(immutable_list_0, immutable_list_2)
    assert (
        f"{type(var_2).__module__}.{type(var_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_2) == 0
    var_0.map(var_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    complex_0 = 2515.121099 - 2135.90079j
    none_type_0 = None
    immutable_list_0 = module_0.ImmutableList(none_type_0)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    immutable_list_0.filter(complex_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    bool_0 = False
    immutable_list_0 = module_0.ImmutableList(tail=bool_0, is_empty=bool_0)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    int_0 = -386
    str_0 = "}xZ\n1X#N7)CJ7~Pfo"
    immutable_list_1 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    immutable_list_2 = immutable_list_1.append(str_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 0
    immutable_list_3 = immutable_list_2.append(int_0)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 0
    var_0 = immutable_list_3.__len__()
    assert var_0 == 0
    immutable_list_3.filter(var_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    none_type_0 = None
    immutable_list_0 = module_0.ImmutableList(none_type_0, none_type_0)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    immutable_list_1 = module_0.ImmutableList(tail=none_type_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    var_0 = immutable_list_1.find(immutable_list_1)
    immutable_list_0.filter(var_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    bool_0 = True
    immutable_list_0 = module_0.ImmutableList(bool_0, bool_0)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert immutable_list_0.head is True
    assert immutable_list_0.tail is True
    assert immutable_list_0.is_empty is False
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    immutable_list_0.find(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    var_0 = immutable_list_0.find(immutable_list_0)
    var_1 = immutable_list_0.reduce(var_0, immutable_list_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_1) == 0
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    immutable_list_0.filter(immutable_list_1)


@pytest.mark.xfail(strict=True)
def test_case_14():
    dict_0 = {}
    none_type_0 = None
    immutable_list_0 = module_0.ImmutableList(dict_0, none_type_0, dict_0)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 1
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    var_0 = immutable_list_0.__len__()
    assert var_0 == 1
    immutable_list_0.reduce(var_0, var_0)


def test_case_15():
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )


def test_case_16():
    none_type_0 = None
    immutable_list_0 = module_0.ImmutableList(none_type_0, is_empty=none_type_0)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    immutable_list_1 = immutable_list_0.__add__(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    immutable_list_2 = immutable_list_0.append(immutable_list_1)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 0
    immutable_list_3 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1
    var_0 = immutable_list_0.__len__()
    assert var_0 == 0
    str_0 = immutable_list_0.__str__()
    assert str_0 == "ImmutableList[None]"


@pytest.mark.xfail(strict=True)
def test_case_17():
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    var_0 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_0) == 1
    immutable_list_0.filter(var_0)


@pytest.mark.xfail(strict=True)
def test_case_18():
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    immutable_list_1 = module_0.ImmutableList(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    immutable_list_2 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    immutable_list_3 = module_0.ImmutableList(immutable_list_1)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1
    bool_0 = immutable_list_1.__eq__(immutable_list_3)
    assert bool_0 is False
    int_0 = -1042
    var_0 = immutable_list_0.find(int_0)
    str_0 = immutable_list_1.__str__()
    immutable_list_4 = immutable_list_2.append(immutable_list_2)
    assert (
        f"{type(immutable_list_4).__module__}.{type(immutable_list_4).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_4) == 1
    immutable_list_1.map(str_0)


@pytest.mark.xfail(strict=True)
def test_case_19():
    bool_0 = False
    immutable_list_0 = module_0.ImmutableList(bool_0, bool_0)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert immutable_list_0.head is False
    assert immutable_list_0.tail is False
    assert immutable_list_0.is_empty is False
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    var_0 = immutable_list_0.append(bool_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert var_0.head is False
    assert (
        f"{type(var_0.tail).__module__}.{type(var_0.tail).__qualname__}"
        == "builtins.NotImplementedType"
    )
    assert var_0.is_empty is False
    var_0.find(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_20():
    immutable_list_0 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    immutable_list_1 = module_0.ImmutableList(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    immutable_list_2 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    immutable_list_3 = module_0.ImmutableList(immutable_list_1)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1
    bool_0 = immutable_list_1.__eq__(immutable_list_3)
    assert bool_0 is False
    immutable_list_1.find(immutable_list_0)


@pytest.mark.xfail(strict=True)
def test_case_21():
    none_type_0 = None
    bool_0 = True
    immutable_list_0 = module_0.ImmutableList(tail=none_type_0, is_empty=bool_0)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    immutable_list_1 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    bool_1 = immutable_list_1.__eq__(bool_0)
    assert bool_1 is False
    bool_2 = immutable_list_1.__eq__(immutable_list_1)
    assert bool_2 is True
    immutable_list_2 = immutable_list_1.unshift(none_type_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 0
    immutable_list_3 = immutable_list_1.unshift(immutable_list_2)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1
    var_0 = immutable_list_0.__len__()
    assert var_0 == 0
    int_0 = -1042
    str_0 = immutable_list_1.__str__()
    assert str_0 == "ImmutableList[None]"
    immutable_list_4 = immutable_list_3.append(int_0)
    assert (
        f"{type(immutable_list_4).__module__}.{type(immutable_list_4).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_4) == 1
    immutable_list_5 = immutable_list_0.__add__(immutable_list_3)
    assert (
        f"{type(immutable_list_5).__module__}.{type(immutable_list_5).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_5) == 0
    immutable_list_4.reduce(var_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_22():
    none_type_0 = None
    bool_0 = True
    immutable_list_0 = module_0.ImmutableList(tail=none_type_0, is_empty=bool_0)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_0) == 0
    assert (
        f"{type(module_0.T).__module__}.{type(module_0.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.U).__module__}.{type(module_0.U).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_0.ImmutableList.of).__module__}.{type(module_0.ImmutableList.of).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.ImmutableList.empty).__module__}.{type(module_0.ImmutableList.empty).__qualname__}"
        == "builtins.method"
    )
    bool_1 = immutable_list_0.__eq__(immutable_list_0)
    assert bool_1 is True
    immutable_list_1 = immutable_list_0.unshift(none_type_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    immutable_list_2 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    var_0 = immutable_list_2.__len__()
    assert var_0 == 1
    bool_2 = immutable_list_1.__eq__(immutable_list_0)
    assert bool_2 is False
    immutable_list_2.find(var_0)