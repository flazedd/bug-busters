# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import immutable_list as module_0
import typing as module_1
import builtins as module_2


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
    var_0 = immutable_list_0.__len__()
    assert var_0 == 0
    immutable_list_1 = immutable_list_0.unshift(bool_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    immutable_list_1.find(immutable_list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    immutable_list_0 = module_0.ImmutableList(bool_0, bool_0, bool_0)
    assert (
        f"{type(immutable_list_0).__module__}.{type(immutable_list_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert immutable_list_0.head is True
    assert immutable_list_0.tail is True
    assert immutable_list_0.is_empty is True
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
    bool_1 = immutable_list_0.__eq__(bool_0)
    assert bool_1 is False
    immutable_list_0.to_list()


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
    var_0 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_0) == 1


def test_case_3():
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
    var_0 = immutable_list_1.to_list()
    var_1 = immutable_list_0.to_list()
    immutable_list_2 = var_1.append(immutable_list_1)
    with pytest.raises(ValueError):
        immutable_list_0.__add__(var_0)


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


def test_case_5():
    int_0 = -1857
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
    immutable_list_1 = immutable_list_0.unshift(int_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    var_0 = immutable_list_1.to_list()
    immutable_list_2 = immutable_list_0.unshift(int_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    var_1 = immutable_list_2.__len__()
    assert var_1 == 1
    immutable_list_3 = immutable_list_2.__add__(immutable_list_2)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1


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
    generic_0 = module_1.Generic()
    assert (
        f"{type(generic_0).__module__}.{type(generic_0).__qualname__}"
        == "typing.Generic"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
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
    immutable_list_0.map(var_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
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
    immutable_list_1 = immutable_list_0.append(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    var_1 = immutable_list_0.__len__()
    assert var_1 == 0
    immutable_list_1.map(var_0)


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
    var_0 = immutable_list_0.reduce(immutable_list_0, immutable_list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_0) == 0
    immutable_list_0.filter(immutable_list_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
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
    none_type_0 = None
    var_0 = immutable_list_0.__len__()
    assert var_0 == 0
    immutable_list_1 = immutable_list_0.append(none_type_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    var_1 = immutable_list_1.to_list()
    immutable_list_1.filter(var_0)


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
    none_type_0 = None
    none_type_1 = None
    immutable_list_1 = module_0.ImmutableList(tail=none_type_1, is_empty=none_type_1)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    var_0 = immutable_list_1.find(none_type_0)
    bool_0 = var_0.__eq__(immutable_list_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    none_type_0 = None
    bool_0 = False
    immutable_list_0 = module_0.ImmutableList(none_type_0, is_empty=bool_0)
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
    var_0 = immutable_list_1.find(none_type_0)
    complex_0 = 1341.7 + 1352.419405j
    immutable_list_2 = module_0.ImmutableList(complex_0, none_type_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    immutable_list_2.reduce(none_type_0, none_type_0)


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
    str_0 = immutable_list_0.__str__()
    assert str_0 == "ImmutableList[None]"


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
    bool_0 = immutable_list_0.__eq__(immutable_list_0)
    assert bool_0 is True
    bool_1 = False
    immutable_list_1 = immutable_list_0.append(bool_1)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    var_0 = immutable_list_0.__len__()
    assert var_0 == 0
    var_1 = immutable_list_0.__len__()
    assert var_1 == 0
    immutable_list_2 = var_1.__add__(var_1)
    assert immutable_list_2 == 0


@pytest.mark.xfail(strict=True)
def test_case_16():
    bool_0 = True
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
    var_0.to_list()


@pytest.mark.xfail(strict=True)
def test_case_17():
    bool_0 = False
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
    str_0 = immutable_list_0.__str__()
    assert str_0 == "ImmutableList[None]"
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    bool_1 = immutable_list_0.__eq__(bool_0)
    assert bool_1 is False
    immutable_list_1.reduce(str_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_18():
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
    immutable_list_1 = module_0.ImmutableList(none_type_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    immutable_list_2 = immutable_list_0.__add__(immutable_list_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 0
    immutable_list_3 = immutable_list_1.__add__(immutable_list_1)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 0
    bool_0 = immutable_list_0.__eq__(immutable_list_3)
    assert bool_0 is False
    var_0 = immutable_list_1.to_list()
    var_0.map(none_type_0)


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
    bool_0 = False
    var_0 = immutable_list_0.reduce(bool_0, immutable_list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_0) == 0
    var_1 = immutable_list_0.find(var_0)
    var_2 = immutable_list_0.reduce(var_1, immutable_list_0)
    assert (
        f"{type(var_2).__module__}.{type(var_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_2) == 0
    var_3 = immutable_list_0.to_list()
    var_4 = var_3.__len__()
    assert var_4 == 1
    var_5 = immutable_list_0.__len__()
    assert var_5 == 0
    var_6 = immutable_list_0.__len__()
    assert var_6 == 0
    immutable_list_1 = immutable_list_0.unshift(var_3)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    immutable_list_2 = module_0.ImmutableList(var_6)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    immutable_list_3 = module_0.ImmutableList(var_3)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1
    bool_1 = immutable_list_0.__eq__(immutable_list_1)
    assert bool_1 is False
    var_5.reduce(immutable_list_2, immutable_list_0)


@pytest.mark.xfail(strict=True)
def test_case_20():
    int_0 = 0
    object_0 = module_2.object()
    bool_0 = True
    immutable_list_0 = module_0.ImmutableList(object_0, is_empty=bool_0)
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
    immutable_list_0.find(int_0)