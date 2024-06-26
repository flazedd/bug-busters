# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import unique as module_0


def test_case_0():
    str_0 = "P\nJ_ Xs\\S\x0bQb*^\nK"
    uniqueness_0 = module_0.Uniqueness(str_0)
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
    bool_0 = uniqueness_0.__contains__(str_0)
    assert bool_0 is False
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    bool_1 = uniqueness_1.__contains__(str_0)
    assert bool_1 is False
    bytes_0 = b"\xb0\xa6%\xed%\xf5\xfb\xdd\xe9\xd8*"
    uniqueness_2 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_2).__module__}.{type(uniqueness_2).__qualname__}"
        == "unique.Uniqueness"
    )
    with pytest.raises(AssertionError):
        uniqueness_2.make_hashable(bytes_0)


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
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    uniqueness_1.add(uniqueness_0)


@pytest.mark.xfail(strict=True)
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
    bool_0 = uniqueness_0.__contains__(none_type_0)
    assert bool_0 is False
    none_type_1 = uniqueness_0.add(none_type_0)
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    none_type_2 = uniqueness_0.add(none_type_0)
    uniqueness_1.__contains__(uniqueness_0)


def test_case_3():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
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
        uniqueness_0.make_hashable(list_0)


def test_case_4():
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
    bool_0 = uniqueness_0.__contains__(list_0)
    assert bool_0 is False
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    with pytest.raises(AssertionError):
        uniqueness_1.make_hashable(uniqueness_1)


def test_case_5():
    str_0 = '<z/tg")o%\x0b,Ro\x0b'
    dict_0 = {str_0: str_0}
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
    none_type_0 = uniqueness_0.add(dict_0)


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
    uniqueness_1 = module_0.Uniqueness()
    assert (
        f"{type(uniqueness_1).__module__}.{type(uniqueness_1).__qualname__}"
        == "unique.Uniqueness"
    )
    uniqueness_1.__contains__(uniqueness_1)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b"\x8a\xea0M@N\x14\xc4\xed#\xd9\x89g\x92P"
    dict_0 = {bytes_0: bytes_0}
    list_0 = [dict_0]
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
    var_0.make_hashable(list_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    bool_0 = False
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
    var_0.make_hashable(bool_0)
