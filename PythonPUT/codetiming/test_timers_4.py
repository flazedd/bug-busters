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
    str_0 = "\r16$;wR*"
    timers_0.total(str_0)


def test_case_2():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "!8'\x0cxvd1F+"
    with pytest.raises(KeyError):
        timers_0.stdev(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "slx:QqMoxA]zwP"
    float_0 = -1183.951819
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.stdev(str_0)
    timers_0.count(float_0)


def test_case_4():
    list_0 = []
    dict_0 = {}
    timers_0 = module_0.Timers(*list_0, **dict_0)
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = timers_0.clear()


@pytest.mark.xfail(strict=True)
def test_case_5():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "}"
    dict_0 = {str_0: str_0}
    timers_0.update(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    float_0 = timers_0.copy()
    assert f"{type(float_0).__module__}.{type(float_0).__qualname__}" == "timers.Timers"
    assert len(float_0) == 0
    str_0 = ":2"
    timers_1 = module_0.Timers()
    assert (
        f"{type(timers_1).__module__}.{type(timers_1).__qualname__}" == "timers.Timers"
    )
    assert len(timers_1) == 0
    timers_0.min(str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "DJ8R<%;C-&pjS"
    timers_0.max(str_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "Qlx:QqaoxA]zwP"
    float_0 = -1183.951819
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.stdev(str_0)
    timers_0.mean(float_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    timers_0.median(none_type_0)


def test_case_10():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "slx:QqMoxA]zwP"
    float_0 = -1183.951819
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.max(str_0)
    assert float_1 == pytest.approx(-1183.951819, abs=0.01, rel=0.01)
    float_2 = timers_0.stdev(str_0)


def test_case_11():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "slx:QqMoxA]zwP"
    float_0 = -1183.951819
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.max(str_0)
    assert float_1 == pytest.approx(-1183.951819, abs=0.01, rel=0.01)
    float_2 = timers_0.median(str_0)
    assert float_2 == pytest.approx(-1183.951819, abs=0.01, rel=0.01)
    float_3 = timers_0.stdev(str_0)
    float_4 = timers_0.count(str_0)
    assert float_4 == 1
    timers_1 = module_0.Timers()
    assert (
        f"{type(timers_1).__module__}.{type(timers_1).__qualname__}" == "timers.Timers"
    )
    assert len(timers_1) == 0
    float_5 = timers_0.min(str_0)
    assert float_5 == pytest.approx(-1183.951819, abs=0.01, rel=0.01)
    str_1 = "+~I''#z]P*'\\Wu"
    with pytest.raises(KeyError):
        timers_0.stdev(str_1)


@pytest.mark.xfail(strict=True)
def test_case_12():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "lx:QqMoA]zw"
    float_0 = -1183.951819
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.max(str_0)
    assert float_1 == pytest.approx(-1183.951819, abs=0.01, rel=0.01)
    float_2 = timers_0.median(str_0)
    assert float_2 == pytest.approx(-1183.951819, abs=0.01, rel=0.01)
    bool_0 = True
    none_type_1 = timers_0.add(str_0, bool_0)
    float_3 = timers_0.stdev(str_0)
    assert float_3 == pytest.approx(837.8874665942344, abs=0.01, rel=0.01)
    none_type_2 = timers_0.clear()
    assert len(timers_0) == 0
    str_1 = "nOhrD"
    timers_0.count(str_1)


@pytest.mark.xfail(strict=True)
def test_case_13():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "slx:QbMoxA]zwP"
    float_0 = -1183.951819
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.median(str_0)
    assert float_1 == pytest.approx(-1183.951819, abs=0.01, rel=0.01)
    float_2 = timers_0.min(str_0)
    assert float_2 == pytest.approx(-1183.951819, abs=0.01, rel=0.01)
    float_3 = timers_0.mean(str_0)
    assert float_3 == pytest.approx(-1183.951819, abs=0.01, rel=0.01)
    float_4 = timers_0.stdev(str_0)
    float_5 = timers_0.count(str_0)
    assert float_5 == 1
    timers_0.pop(none_type_0)