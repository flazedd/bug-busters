# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import unique as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"z\xf69R\xde\xdd"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.Uniqueness(dict_0)


def test_case_1():
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
    bool_0 = uniqueness_0.__contains__(none_type_0)
    assert bool_0 is False


def test_case_2():
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
    none_type_0 = None
    uniqueness_1 = module_0.Uniqueness(none_type_0)
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    with pytest.raises(AssertionError):
        uniqueness_0.make_hashable(uniqueness_0)


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
    bool_0 = False
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    var_0 = uniqueness_1.make_hashable(bool_0)
    bool_1 = True
    uniqueness_2 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_2).__module__}.{type(uniqueness_2).__qualname__}"
        == "unique.Uniqueness"
    )
    list_0 = [bool_1, bool_1, bool_1]
    uniqueness_3 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_3).__module__}.{type(uniqueness_3).__qualname__}"
        == "unique.Uniqueness"
    )
    var_1 = uniqueness_3.make_hashable(list_0)


def test_case_4():
    none_type_0 = None
    uniqueness_0 = module_0.Uniqueness(none_type_0)
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
    dict_0 = {uniqueness_0: none_type_0}
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    with pytest.raises(AssertionError):
        uniqueness_1.make_hashable(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 2189.3
    none_type_0 = None
    uniqueness_0 = module_0.Uniqueness(none_type_0)
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
    dict_0 = {}
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    var_0 = uniqueness_1.make_hashable(dict_0)
    var_0.make_hashable(float_0)


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
    uniqueness_0.add(uniqueness_0)


@pytest.mark.xfail(strict=True)
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
    float_0 = 2163.8
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    var_0 = uniqueness_1.make_hashable(float_0)
    assert var_0 == pytest.approx(2163.8, abs=0.01, rel=0.01)
    var_0.__contains__(uniqueness_0)
