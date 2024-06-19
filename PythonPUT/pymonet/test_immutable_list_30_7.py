# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import immutable_list as module_0
import builtins as module_1
import typing as module_2


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
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    bool_0 = immutable_list_0.__eq__(immutable_list_0)
    assert bool_0 is True
    var_0 = immutable_list_0.to_list()
    immutable_list_2 = module_0.ImmutableList(tail=immutable_list_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 0
    immutable_list_1.find(immutable_list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    bytes_0 = b"\xdb\x8f\x88\xd2\x8d4F\x1e}J"
    bool_0 = True
    immutable_list_0 = module_0.ImmutableList(bytes_0, is_empty=bool_0)
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
    bool_1 = immutable_list_0.__eq__(object_0)
    assert bool_1 is False
    immutable_list_1 = module_0.ImmutableList(bool_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    none_type_0 = None
    immutable_list_0.reduce(immutable_list_0, none_type_0)


def test_case_2():
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
    with pytest.raises(ValueError):
        immutable_list_0.__add__(none_type_0)


def test_case_3():
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
    var_0 = immutable_list_0.find(bool_0)
    var_1 = immutable_list_0.__len__()
    assert var_1 == 0


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
    immutable_list_1 = module_0.ImmutableList(immutable_list_0, immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    none_type_0 = None
    var_0 = immutable_list_1.__len__()
    assert var_0 == 1
    int_0 = -2639
    immutable_list_1.reduce(none_type_0, int_0)


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
    immutable_list_1 = module_0.ImmutableList(immutable_list_0, immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    var_0 = immutable_list_1.to_list()
    immutable_list_1.find(var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
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
    immutable_list_0.map(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
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
    var_1 = immutable_list_0.__len__()
    assert var_1 == 0
    bool_0 = immutable_list_0.__eq__(immutable_list_0)
    assert bool_0 is True
    var_2 = immutable_list_0.find(immutable_list_0)
    none_type_0 = None
    immutable_list_1 = immutable_list_0.append(none_type_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    str_0 = immutable_list_0.__str__()
    assert str_0 == "ImmutableList[None]"
    immutable_list_1.map(none_type_0)


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
    immutable_list_0.filter(immutable_list_0)


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
    immutable_list_0.filter(var_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    object_0 = module_1.object()
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
    none_type_0 = None
    immutable_list_0.reduce(immutable_list_0, none_type_0)


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


def test_case_12():
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
    str_0 = immutable_list_0.__str__()
    assert str_0 == "ImmutableList[None]"
    var_0 = immutable_list_0.to_list()
    var_1 = immutable_list_0.find(var_0)
    var_2 = immutable_list_0.reduce(var_1, str_0)
    assert var_2 == "ImmutableList[None]"
    var_3 = module_2.Generic()
    assert f"{type(var_3).__module__}.{type(var_3).__qualname__}" == "typing.Generic"
    assert module_2.EXCLUDED_ATTRIBUTES == [
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
        f"{type(module_2.T).__module__}.{type(module_2.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.KT).__module__}.{type(module_2.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.VT).__module__}.{type(module_2.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.T_co).__module__}.{type(module_2.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.V_co).__module__}.{type(module_2.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.VT_co).__module__}.{type(module_2.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.T_contra).__module__}.{type(module_2.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.CT_co).__module__}.{type(module_2.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.AnyStr).__module__}.{type(module_2.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_2.TYPE_CHECKING is False
    immutable_list_1 = immutable_list_0.unshift(var_3)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    var_4 = immutable_list_0.to_list()


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
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    bool_0 = immutable_list_0.__eq__(immutable_list_0)
    assert bool_0 is True
    var_0 = immutable_list_0.find(immutable_list_0)
    immutable_list_2 = immutable_list_0.append(immutable_list_1)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 0
    str_0 = immutable_list_0.__str__()
    assert str_0 == "ImmutableList[None]"
    immutable_list_2.filter(var_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    bool_0 = True
    none_type_0 = None
    immutable_list_0 = module_0.ImmutableList(is_empty=none_type_0)
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
    var_0 = immutable_list_0.reduce(bool_0, bool_0)
    assert var_0 is True
    immutable_list_1 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    immutable_list_2 = immutable_list_1.unshift(var_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    immutable_list_3 = immutable_list_2.append(var_0)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1
    immutable_list_3.find(var_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
    bool_0 = True
    none_type_0 = None
    immutable_list_0 = module_0.ImmutableList(is_empty=none_type_0)
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
    var_0 = immutable_list_0.reduce(bool_0, bool_0)
    assert var_0 is True
    immutable_list_1 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    immutable_list_2 = module_0.ImmutableList(immutable_list_0, is_empty=bool_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    var_1 = immutable_list_2.__len__()
    assert var_1 == 1
    var_2 = immutable_list_1.__len__()
    assert var_2 == 0
    bool_1 = immutable_list_1.__eq__(immutable_list_1)
    assert bool_1 is True
    immutable_list_3 = immutable_list_2.append(var_0)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 2
    str_0 = var_0.__str__()
    assert str_0 == "True"
    immutable_list_3.find(var_1)


@pytest.mark.xfail(strict=True)
def test_case_16():
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
    immutable_list_1 = immutable_list_0.__add__(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    var_1 = immutable_list_0.find(var_0)
    bool_0 = immutable_list_0.__eq__(immutable_list_1)
    assert bool_0 is False
    var_1.find(var_0)


@pytest.mark.xfail(strict=True)
def test_case_17():
    str_0 = "n}n1e:D2fT-:\t8>=E-"
    list_0 = [str_0, str_0]
    immutable_list_0 = module_0.ImmutableList(list_0)
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
    immutable_list_0.find(immutable_list_0)


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
    immutable_list_1 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    bool_0 = immutable_list_0.__eq__(immutable_list_1)
    assert bool_0 is False
    immutable_list_1.find(immutable_list_1)
