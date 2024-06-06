# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import unique as module_0


def test_case_0():
    bytes_0 = b"w\xdb\x00\x94"
    uniqueness_0 = module_0.Uniqueness(bytes_0)
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
        uniqueness_0.make_hashable(bytes_0)


@pytest.mark.xfail(strict=True)
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
    uniqueness_0.__contains__(uniqueness_0)


def test_case_2():
    none_type_0 = None
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
    var_0 = uniqueness_0.make_hashable(none_type_0)
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    none_type_1 = None
    none_type_2 = uniqueness_1.add(none_type_1)
    with pytest.raises(AssertionError):
        uniqueness_0.make_hashable(uniqueness_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 874.849592
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
    list_0 = [dict_0, float_0]
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
    none_type_0 = uniqueness_0.add(float_0)
    bool_0 = False
    tuple_0 = (dict_0, list_0, bool_0)
    bool_1 = False
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    var_0 = uniqueness_1.make_hashable(list_0)
    var_1 = uniqueness_1.make_hashable(bool_1)
    var_1.make_hashable(tuple_0)


def test_case_4():
    bytes_0 = b"\x9b\xd1\x19|UjdG\x07(\xaa\xb4\xcb\xd4p\xbc"
    dict_0 = {bytes_0: bytes_0}
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
        uniqueness_0.make_hashable(dict_0)


def test_case_5():
    dict_0 = {}
    uniqueness_0 = module_0.Uniqueness(dict_0)
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
    bool_0 = uniqueness_0.__contains__(dict_0)
    assert bool_0 is False
    bool_1 = True
    var_0 = uniqueness_0.make_hashable(bool_1)
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    uniqueness_2 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_2).__module__}.{type(uniqueness_2).__qualname__}"
        == "unique.Uniqueness"
    )
    var_1 = uniqueness_0.make_hashable(dict_0)
    with pytest.raises(AssertionError):
        uniqueness_2.make_hashable(uniqueness_2)


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = -3477
    none_type_0 = None
    none_type_1 = None
    uniqueness_0 = module_0.Uniqueness(none_type_1)
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
    var_0 = uniqueness_0.make_hashable(int_0)
    assert var_0 == -3477
    var_0.make_hashable(none_type_0)