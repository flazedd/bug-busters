# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import timers as module_0


def test_case_0():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    bool_0 = False
    none_type_1 = timers_0.add(none_type_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.median(none_type_0)
    assert float_0 is False
    str_0 = "i0m[&e$QN$2\tw '"
    timers_0.count(str_0)


def test_case_2():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "NnDnaI*6mD"
    with pytest.raises(KeyError):
        timers_0.stdev(str_0)


def test_case_3():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    bool_0 = False
    none_type_1 = timers_0.add(none_type_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.max(none_type_0)
    assert float_0 is False


def test_case_4():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    bool_0 = False
    none_type_1 = timers_0.add(none_type_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.median(none_type_0)
    assert float_0 is False
    float_1 = timers_0.clear()
    assert len(timers_0) == 0


@pytest.mark.xfail(strict=True)
def test_case_5():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    timers_0.__setitem__(timers_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.total(timers_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    bool_0 = False
    none_type_1 = timers_0.add(none_type_0, bool_0)
    assert len(timers_0) == 1
    var_0 = timers_0.update()
    var_1 = timers_0.items()
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "collections.abc.ItemsView"
    )
    assert len(var_1) == 1
    float_0 = timers_0.min(var_0)
    assert float_0 is False
    var_0.stdev(var_0)


def test_case_8():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    bool_0 = False
    none_type_1 = timers_0.add(none_type_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.median(none_type_0)
    assert float_0 is False


def test_case_9():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    bool_0 = False
    none_type_1 = timers_0.add(none_type_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.stdev(none_type_0)
    var_0 = timers_0.update()
    float_1 = timers_0.mean(none_type_0)
    assert float_1 == 0


def test_case_10():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    bool_0 = False
    none_type_1 = timers_0.add(none_type_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.stdev(none_type_0)
    float_1 = timers_0.max(none_type_0)
    assert float_1 is False


@pytest.mark.xfail(strict=True)
def test_case_11():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    bool_0 = False
    none_type_1 = timers_0.add(none_type_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.stdev(none_type_0)
    var_0 = timers_0.update()
    none_type_2 = timers_0.add(var_0, float_0)
    float_1 = timers_0.stdev(var_0)
    str_0 = "ik'gLnz.{4EGVC"
    var_0.max(str_0)
