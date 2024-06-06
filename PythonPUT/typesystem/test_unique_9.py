# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import unique as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    uniqueness_0 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_0).__module__}.{type(uniqueness_0).__qualname__}"
        == "unique.Uniqueness"
    )
    assert (
        f"{type(module_0.Uniqueness.TRUE).__module__}.{type(module_0.Uniqueness.TRUE).__qualname__}"
        == "builtins.object"
    )
    assert (
        f"{type(module_0.Uniqueness.FALSE).__module__}.{type(module_0.Uniqueness.FALSE).__qualname__}"
        == "builtins.object"
    )
    var_0 = uniqueness_0.make_hashable(list_0)
    str_0 = "@/jOKd0IgI"
    tuple_0 = (var_0, var_0, var_0, str_0)
    list_1 = [list_0, tuple_0]
    module_0.Uniqueness(list_1)


def test_case_1():
    uniqueness_0 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_0).__module__}.{type(uniqueness_0).__qualname__}"
        == "unique.Uniqueness"
    )
    assert (
        f"{type(module_0.Uniqueness.TRUE).__module__}.{type(module_0.Uniqueness.TRUE).__qualname__}"
        == "builtins.object"
    )
    assert (
        f"{type(module_0.Uniqueness.FALSE).__module__}.{type(module_0.Uniqueness.FALSE).__qualname__}"
        == "builtins.object"
    )


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "zKBn`),[arJ"
    none_type_0 = None
    bool_0 = False
    uniqueness_0 = module_0.Uniqueness(bool_0)
    assert (
        f"{type(uniqueness_0).__module__}.{type(uniqueness_0).__qualname__}"
        == "unique.Uniqueness"
    )
    assert (
        f"{type(module_0.Uniqueness.TRUE).__module__}.{type(module_0.Uniqueness.TRUE).__qualname__}"
        == "builtins.object"
    )
    assert (
        f"{type(module_0.Uniqueness.FALSE).__module__}.{type(module_0.Uniqueness.FALSE).__qualname__}"
        == "builtins.object"
    )
    var_0 = uniqueness_0.make_hashable(none_type_0)
    var_0.add(str_0)


def test_case_3():
    uniqueness_0 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_0).__module__}.{type(uniqueness_0).__qualname__}"
        == "unique.Uniqueness"
    )
    assert (
        f"{type(module_0.Uniqueness.TRUE).__module__}.{type(module_0.Uniqueness.TRUE).__qualname__}"
        == "builtins.object"
    )
    assert (
        f"{type(module_0.Uniqueness.FALSE).__module__}.{type(module_0.Uniqueness.FALSE).__qualname__}"
        == "builtins.object"
    )
    with pytest.raises(AssertionError):
        uniqueness_0.make_hashable(uniqueness_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0]
    uniqueness_0 = module_0.Uniqueness(list_0)
    assert (
        f"{type(uniqueness_0).__module__}.{type(uniqueness_0).__qualname__}"
        == "unique.Uniqueness"
    )
    assert (
        f"{type(module_0.Uniqueness.TRUE).__module__}.{type(module_0.Uniqueness.TRUE).__qualname__}"
        == "builtins.object"
    )
    assert (
        f"{type(module_0.Uniqueness.FALSE).__module__}.{type(module_0.Uniqueness.FALSE).__qualname__}"
        == "builtins.object"
    )
    var_0 = uniqueness_0.make_hashable(list_0)
    str_0 = "e\r!hWS$k2dT1l<3W"
    bytes_0 = b"g\x08\x95\x89"
    uniqueness_1 = module_0.Uniqueness(str_0)
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    var_1 = uniqueness_1.make_hashable(str_0)
    assert var_1 == "e\r!hWS$k2dT1l<3W"
    var_1.make_hashable(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = -2921
    uniqueness_0 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_0).__module__}.{type(uniqueness_0).__qualname__}"
        == "unique.Uniqueness"
    )
    assert (
        f"{type(module_0.Uniqueness.TRUE).__module__}.{type(module_0.Uniqueness.TRUE).__qualname__}"
        == "builtins.object"
    )
    assert (
        f"{type(module_0.Uniqueness.FALSE).__module__}.{type(module_0.Uniqueness.FALSE).__qualname__}"
        == "builtins.object"
    )
    none_type_0 = uniqueness_0.add(int_0)
    dict_0 = {int_0: int_0}
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    str_0 = ""
    var_0 = uniqueness_1.make_hashable(dict_0)
    tuple_0 = (uniqueness_1, str_0)
    str_1 = ";E97c`Nt['Ms{o"
    var_1 = uniqueness_0.make_hashable(str_1)
    assert var_1 == ";E97c`Nt['Ms{o"
    uniqueness_1.__contains__(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    uniqueness_0 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_0).__module__}.{type(uniqueness_0).__qualname__}"
        == "unique.Uniqueness"
    )
    assert (
        f"{type(module_0.Uniqueness.TRUE).__module__}.{type(module_0.Uniqueness.TRUE).__qualname__}"
        == "builtins.object"
    )
    assert (
        f"{type(module_0.Uniqueness.FALSE).__module__}.{type(module_0.Uniqueness.FALSE).__qualname__}"
        == "builtins.object"
    )
    uniqueness_0.__contains__(uniqueness_0)


def test_case_7():
    uniqueness_0 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_0).__module__}.{type(uniqueness_0).__qualname__}"
        == "unique.Uniqueness"
    )
    assert (
        f"{type(module_0.Uniqueness.TRUE).__module__}.{type(module_0.Uniqueness.TRUE).__qualname__}"
        == "builtins.object"
    )
    assert (
        f"{type(module_0.Uniqueness.FALSE).__module__}.{type(module_0.Uniqueness.FALSE).__qualname__}"
        == "builtins.object"
    )
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    none_type_0 = None
    none_type_1 = uniqueness_0.add(none_type_0)
    var_0 = uniqueness_0.make_hashable(none_type_0)
    none_type_2 = None
    uniqueness_2 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_2).__module__}.{type(uniqueness_2).__qualname__}"
        == "unique.Uniqueness"
    )
    none_type_3 = uniqueness_2.add(none_type_2)


@pytest.mark.xfail(strict=True)
def test_case_8():
    bool_0 = True
    uniqueness_0 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_0).__module__}.{type(uniqueness_0).__qualname__}"
        == "unique.Uniqueness"
    )
    assert (
        f"{type(module_0.Uniqueness.TRUE).__module__}.{type(module_0.Uniqueness.TRUE).__qualname__}"
        == "builtins.object"
    )
    assert (
        f"{type(module_0.Uniqueness.FALSE).__module__}.{type(module_0.Uniqueness.FALSE).__qualname__}"
        == "builtins.object"
    )
    var_0 = uniqueness_0.make_hashable(bool_0)
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    none_type_0 = None
    uniqueness_1 = module_0.Uniqueness(none_type_0)
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    none_type_1 = uniqueness_1.add(none_type_0)
    uniqueness_1.add(set_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = ""
    uniqueness_0 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_0).__module__}.{type(uniqueness_0).__qualname__}"
        == "unique.Uniqueness"
    )
    assert (
        f"{type(module_0.Uniqueness.TRUE).__module__}.{type(module_0.Uniqueness.TRUE).__qualname__}"
        == "builtins.object"
    )
    assert (
        f"{type(module_0.Uniqueness.FALSE).__module__}.{type(module_0.Uniqueness.FALSE).__qualname__}"
        == "builtins.object"
    )
    none_type_0 = uniqueness_0.add(str_0)
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    bool_0 = False
    bool_1 = uniqueness_0.__contains__(bool_0)
    assert bool_1 is False
    none_type_1 = None
    bool_2 = uniqueness_1.__contains__(none_type_0)
    assert bool_2 is False
    bool_3 = uniqueness_1.__contains__(none_type_1)
    assert bool_3 is False
    uniqueness_1.add(uniqueness_1)