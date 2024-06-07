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
    immutable_list_1 = immutable_list_0.append(bool_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    var_0 = immutable_list_0.__len__()
    assert var_0 == 0
    var_0.__len__()


@pytest.mark.xfail(strict=True)
def test_case_1():
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
    immutable_list_0 = module_0.ImmutableList(is_empty=generic_0)
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
    immutable_list_1 = immutable_list_0.append(generic_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    bool_0 = immutable_list_1.__eq__(none_type_0)
    assert bool_0 is False
    immutable_list_2 = module_0.ImmutableList(bool_0, none_type_0, bool_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    immutable_list_2.find(immutable_list_2)


def test_case_2():
    none_type_0 = None
    list_0 = []
    immutable_list_0 = module_0.ImmutableList(list_0, list_0)
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
    immutable_list_1 = immutable_list_0.unshift(none_type_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0


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
    none_type_0 = None
    with pytest.raises(ValueError):
        immutable_list_0.__add__(none_type_0)


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
    immutable_list_0.filter(var_0)


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
    immutable_list_2 = immutable_list_0.unshift(immutable_list_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    immutable_list_3 = immutable_list_1.append(immutable_list_0)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1
    str_0 = immutable_list_2.__str__()
    var_0 = immutable_list_0.reduce(immutable_list_0, immutable_list_2)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_0) == 1
    var_1 = immutable_list_1.__len__()
    assert var_1 == 1
    var_0.find(var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    immutable_list_0 = module_0.ImmutableList(tail=bool_0)
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
    immutable_list_0.to_list()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = ""
    int_0 = -105
    none_type_0 = None
    bool_0 = False
    immutable_list_0 = module_0.ImmutableList(int_0, none_type_0, bool_0)
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
    immutable_list_0.map(str_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
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
    none_type_0 = None
    none_type_1 = None
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
    immutable_list_1 = immutable_list_0.append(none_type_1)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    var_0 = immutable_list_1.reduce(none_type_0, none_type_0)
    var_1 = immutable_list_1.find(var_0)
    immutable_list_2 = immutable_list_1.unshift(none_type_1)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 0
    bool_0 = True
    var_2 = immutable_list_1.reduce(none_type_1, bool_0)
    assert var_2 is True
    immutable_list_3 = immutable_list_0.append(var_0)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 0
    immutable_list_4 = var_2.__add__(var_2)
    assert immutable_list_4 == 2
    immutable_list_5 = immutable_list_2.unshift(var_2)
    assert (
        f"{type(immutable_list_5).__module__}.{type(immutable_list_5).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_5) == 1
    immutable_list_3.map(var_1)


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
    immutable_list_0 = module_0.ImmutableList(is_empty=generic_0)
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
    str_0 = "h}B%7X\x0b$)+Yv"
    immutable_list_1 = immutable_list_0.append(str_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    var_0 = immutable_list_0.__len__()
    assert var_0 == 0
    var_1 = immutable_list_1.find(none_type_0)
    immutable_list_1.filter(none_type_0)


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
    var_0 = immutable_list_0.reduce(immutable_list_0, immutable_list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_0) == 0
    var_1 = immutable_list_0.find(var_0)
    var_2 = immutable_list_0.find(immutable_list_0)
    immutable_list_1 = var_0.unshift(var_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    var_3 = immutable_list_0.find(immutable_list_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    int_0 = 0
    object_0 = module_2.object()
    immutable_list_0 = module_0.ImmutableList(object_0)
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
    var_0 = immutable_list_0.reduce(immutable_list_0, immutable_list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_0) == 0


def test_case_14():
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
def test_case_15():
    float_0 = -690.03
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
    immutable_list_1 = immutable_list_0.append(immutable_list_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    immutable_list_0.filter(float_0)


@pytest.mark.xfail(strict=True)
def test_case_16():
    bytes_0 = b"\xc3\x96\x1e\x12(\xb7\x93"
    immutable_list_0 = module_0.ImmutableList(bytes_0)
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
    var_0.__len__()


@pytest.mark.xfail(strict=True)
def test_case_17():
    none_type_0 = None
    dict_0 = {}
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
    immutable_list_1 = immutable_list_0.unshift(dict_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 1
    immutable_list_1.find(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_18():
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
    immutable_list_0 = module_0.ImmutableList(is_empty=generic_0)
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
    immutable_list_1 = immutable_list_0.append(generic_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    bool_0 = immutable_list_1.__eq__(none_type_0)
    assert bool_0 is False
    immutable_list_2 = module_0.ImmutableList(bool_0, none_type_0, bool_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    bool_1 = immutable_list_0.__eq__(generic_0)
    assert bool_1 is False
    var_0 = immutable_list_1.__len__()
    assert var_0 == 0
    immutable_list_2.reduce(var_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_19():
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
    immutable_list_0 = module_0.ImmutableList(is_empty=generic_0)
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
    bool_0 = immutable_list_1.__eq__(immutable_list_0)
    assert bool_0 is False
    none_type_0 = None
    immutable_list_2 = immutable_list_0.append(generic_0)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 0
    bool_1 = immutable_list_2.__eq__(none_type_0)
    assert bool_1 is False
    immutable_list_3 = module_0.ImmutableList(bool_1, none_type_0, bool_1)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1
    var_0 = immutable_list_3.__len__()
    assert var_0 == 1
    immutable_list_4 = immutable_list_3.append(bool_1)
    assert (
        f"{type(immutable_list_4).__module__}.{type(immutable_list_4).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_4) == 2
    immutable_list_4.find(immutable_list_3)


@pytest.mark.xfail(strict=True)
def test_case_20():
    str_0 = "`F]$_E"
    immutable_list_0 = module_0.ImmutableList(str_0)
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
    immutable_list_1 = immutable_list_0.unshift(str_0)
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 2
    var_0 = immutable_list_0.__len__()
    assert var_0 == 1
    var_1 = immutable_list_0.append(str_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_1) == 2
    str_1 = immutable_list_0.__str__()
    assert str_1 == "ImmutableList['`F]$_E']"
    var_2 = var_1.__len__()
    assert var_2 == 2
    var_3 = immutable_list_0.__len__()
    assert var_3 == 1
    bytes_0 = b"\xea\x1e\x99Ne"
    var_1.reduce(var_2, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_21():
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
    var_0 = immutable_list_0.reduce(bool_0, immutable_list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(var_0) == 0
    immutable_list_1 = module_0.ImmutableList()
    assert (
        f"{type(immutable_list_1).__module__}.{type(immutable_list_1).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_1) == 0
    immutable_list_2 = module_0.ImmutableList(immutable_list_1)
    assert (
        f"{type(immutable_list_2).__module__}.{type(immutable_list_2).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_2) == 1
    bool_1 = immutable_list_2.__eq__(immutable_list_1)
    assert bool_1 is False
    immutable_list_3 = module_0.ImmutableList(immutable_list_1)
    assert (
        f"{type(immutable_list_3).__module__}.{type(immutable_list_3).__qualname__}"
        == "immutable_list.ImmutableList"
    )
    assert len(immutable_list_3) == 1
    immutable_list_2.find(var_0)
