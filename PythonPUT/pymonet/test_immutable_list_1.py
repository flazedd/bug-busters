# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import immutable_list as module_0


@pytest.mark.xfail(strict=True)
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
    var_0 = immutable_list_0.find(immutable_list_0)
    immutable_list_0.filter(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
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
    bool_0 = immutable_list_0.__eq__(var_0)
    assert bool_0 is False
    var_1 = immutable_list_0.find(var_0)
    immutable_list_0.filter(immutable_list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
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
    immutable_list_1 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    immutable_list_2 = immutable_list_1.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    var_0 = immutable_list_2.to_list()
    immutable_list_2.find(var_0)


def test_case_3():
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
    immutable_list_1 = immutable_list_0.unshift(none_type_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    var_0 = immutable_list_0.to_list()
    var_1 = var_0.__len__()
    assert var_1 == 1
    with pytest.raises(ValueError):
        immutable_list_0.__add__(var_1)


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
    var_0 = immutable_list_0.__len__()
    assert var_0 == 0
    var_1 = immutable_list_0.find(immutable_list_0)
    immutable_list_0.filter(var_1)


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
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    var_0 = immutable_list_1.__len__()
    assert var_0 == 1
    immutable_list_1.find(var_0)


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
    var_0 = immutable_list_0.to_list()


@pytest.mark.xfail(strict=True)
def test_case_7():
    none_type_0 = None
    immutable_list_0 = module_0.ImmutableList(tail=none_type_0)
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
    immutable_list_0.map(immutable_list_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    none_type_0 = None
    bytes_0 = b"\xb3"
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
    immutable_list_1 = module_0.ImmutableList(none_type_0, bytes_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    immutable_list_1.map(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
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
    immutable_list_0.filter(immutable_list_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    bool_0 = True
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
    immutable_list_0.filter(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
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
    immutable_list_0.filter(var_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    bool_0 = True
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
    immutable_list_1.find(bool_0)


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
    var_0 = immutable_list_0.__len__()
    assert var_0 == 0
    var_1 = immutable_list_0.find(var_0)
    bool_0 = var_0.__eq__(immutable_list_0)
    var_2 = immutable_list_0.reduce(var_1, var_1)
    immutable_list_0.filter(var_2)


@pytest.mark.xfail(strict=True)
def test_case_14():
    bool_0 = True
    immutable_list_0 = module_0.ImmutableList(is_empty=bool_0)
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
    immutable_list_1 = module_0.ImmutableList(var_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    immutable_list_1.reduce(var_0, var_0)


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


@pytest.mark.xfail(strict=True)
def test_case_16():
    bool_0 = False
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
    bool_1 = immutable_list_0.__eq__(immutable_list_0)
    assert bool_1 is True
    str_0 = immutable_list_0.__str__()
    assert str_0 == "ImmutableList[None]"
    var_1 = immutable_list_0.find(bool_0)
    immutable_list_0.filter(var_1)


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
    var_0 = immutable_list_0.to_list()
    immutable_list_1 = immutable_list_0.append(var_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    bool_0 = immutable_list_0.__eq__(immutable_list_1)
    assert bool_0 is False
    var_1 = immutable_list_0.find(var_0)
    immutable_list_0.filter(immutable_list_0)


@pytest.mark.xfail(strict=True)
def test_case_18():
    bool_0 = False
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
    bool_1 = immutable_list_1.__eq__(immutable_list_0)
    assert bool_1 is False
    immutable_list_1.find(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_19():
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
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    var_0 = immutable_list_0.to_list()
    immutable_list_2 = immutable_list_1.append(var_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    bool_0 = immutable_list_0.__eq__(immutable_list_1)
    assert bool_0 is False
    immutable_list_1.find(immutable_list_1)


@pytest.mark.xfail(strict=True)
def test_case_20():
    bool_0 = False
    immutable_list_0 = module_0.ImmutableList(bool_0)
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
    immutable_list_0.find(var_0)


@pytest.mark.xfail(strict=True)
def test_case_21():
    float_0 = 930.54989
    immutable_list_0 = module_0.ImmutableList(float_0)
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
    immutable_list_1 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    bool_0 = immutable_list_0.__eq__(float_0)
    assert bool_0 is False
    var_0 = immutable_list_0.__len__()
    assert var_0 == 1
    immutable_list_2 = immutable_list_0.unshift(var_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 2
    immutable_list_2.reduce(var_0, bool_0)
