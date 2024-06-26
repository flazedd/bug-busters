# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import trie as module_0
import builtins as module_1


def test_case_0():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )


@pytest.mark.xfail(strict=True)
def test_case_1():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    var_1 = trie_0.__repr__()
    assert var_1 == "*\n└──*"
    trie_0.repr_brief(var_0, var_0)


def test_case_2():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    none_type_0 = trie_0.insert(trie_0)
    assert len(trie_0) == 1
    with pytest.raises(KeyError):
        trie_0.__getitem__(trie_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    object_0 = module_1.object()
    set_0 = {trie_0}
    trie_0.delete_recursively(trie_0, set_0)


def test_case_4():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    with pytest.raises(KeyError):
        trie_0.__delitem__(trie_0)


def test_case_5():
    str_0 = "Kbt\t?"
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.contains_prefix(str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_6():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.successors(trie_0)
    var_1 = module_0.Trie()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "trie.Trie"
    assert len(var_1) == 0
    trie_0.delete_recursively(var_0, var_0)


def test_case_7():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.__repr__()
    assert var_0 == "*"


@pytest.mark.xfail(strict=True)
def test_case_8():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    object_0 = module_1.object()
    str_0 = "#ot1=fyE(bG"
    trie_0.repr_brief(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    trie_0.delete_recursively(trie_0, trie_0)


def test_case_10():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.successors(trie_0)
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    object_0 = module_1.object()
    var_1 = trie_0.__iter__()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "trie.Trie"
    assert len(var_1) == 1
    var_2 = trie_0.__traverse__(var_0)
    var_3 = trie_1.repr_brief(var_2, var_0)
    assert var_3 == ""
    bool_0 = var_1.__contains__(var_2)
    assert bool_0 is True


@pytest.mark.xfail(strict=True)
def test_case_11():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.__traverse__(trie_0)
    var_1 = trie_0.__iter__()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "trie.Trie"
    assert len(var_1) == 0
    var_2 = var_0.__repr__()
    assert var_2 == "{}"
    none_type_0 = trie_0.insert(var_2)
    assert len(trie_0) == 1
    assert len(var_1) == 1
    var_3 = var_1.successors(var_1)
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_4 = trie_0.__repr__()
    assert var_4 == "*\n└──{\n   └──}"
    var_5 = trie_0.successors(trie_1)
    var_6 = var_1.__delitem__(var_2)
    assert len(trie_0) == 0
    assert len(var_1) == 0
    set_0 = {var_6}
    trie_1.delete_recursively(trie_1, set_0)


def test_case_12():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.__getitem__(trie_0)
    var_1 = trie_0.__repr__()
    assert var_1 == "*"


def test_case_13():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    var_1 = trie_0.__repr__()
    assert var_1 == "*"
    var_2 = trie_0.successors(var_0)


def test_case_14():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    str_0 = "#ot1=fyE(bG"
    var_0 = trie_0.repr_brief(trie_0, str_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_15():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    none_type_0 = trie_0.insert(trie_0)
    assert len(trie_0) == 1
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    object_0 = module_1.object()
    var_0 = trie_1.repr_brief(trie_0, trie_0)
    assert var_0 == ","
    none_type_1 = trie_0.insert(trie_1)
    assert len(trie_0) == 2
    trie_0.__traverse__(none_type_1)


@pytest.mark.xfail(strict=True)
def test_case_16():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.__len__()
    assert var_0 == 0
    var_1 = trie_0.__iter__()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "trie.Trie"
    assert len(var_1) == 0
    var_2 = var_0.__repr__()
    assert var_2 == "0"
    none_type_0 = trie_0.insert(var_2)
    assert len(trie_0) == 1
    assert len(var_1) == 1
    var_3 = var_1.successors(var_1)
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_4 = trie_0.__repr__()
    assert var_4 == "*\n└──0"
    var_5 = trie_0.successors(trie_1)
    var_6 = trie_1.repr_brief(trie_0, var_4)
    assert var_6 == "0"
    var_7 = var_1.__delitem__(var_2)
    assert len(trie_0) == 0
    assert len(var_1) == 0
    set_0 = {var_7}
    trie_1.delete_recursively(trie_1, set_0)


@pytest.mark.xfail(strict=True)
def test_case_17():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.__traverse__(trie_0)
    var_1 = trie_0.__iter__()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "trie.Trie"
    assert len(var_1) == 0
    var_2 = var_0.__repr__()
    assert var_2 == "{}"
    none_type_0 = trie_0.insert(var_2)
    assert len(trie_0) == 1
    assert len(var_1) == 1
    var_3 = var_1.successors(var_1)
    var_4 = trie_0.__repr__()
    assert var_4 == "*\n└──{\n   └──}"
    var_5 = trie_0.successors(var_0)
    var_6 = var_1.repr_brief(trie_0, var_4)
    assert var_6 == "{}"
    var_7 = var_1.__delitem__(var_2)
    assert len(trie_0) == 0
    assert len(var_1) == 0
    set_0 = {var_7}
    var_6.delete_recursively(var_6, set_0)


@pytest.mark.xfail(strict=True)
def test_case_18():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.__len__()
    assert var_0 == 0
    var_1 = trie_0.__iter__()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "trie.Trie"
    assert len(var_1) == 0
    none_type_0 = var_1.insert(var_1)
    assert len(trie_0) == 1
    assert len(var_1) == 1
    var_2 = var_0.__repr__()
    assert var_2 == "0"
    none_type_1 = trie_0.insert(var_2)
    assert len(trie_0) == 2
    assert len(var_1) == 2
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    str_0 = "#odt1=fyE(bG"
    var_3 = trie_0.successors(trie_1)
    var_4 = trie_1.repr_brief(trie_0, str_0)
    assert var_4 == "[#odt1=fyE(bG0,0]"
    var_5 = var_1.__delitem__(var_2)
    assert len(trie_0) == 1
    assert len(var_1) == 1
    var_6 = var_1.contains_prefix(var_3)
    assert var_6 is False
    var_7 = var_4.__len__()
    assert var_7 == 17
    trie_1.delete_recursively(trie_1, var_1)


@pytest.mark.xfail(strict=True)
def test_case_19():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    str_0 = "c"
    none_type_0 = trie_0.insert(str_0)
    assert len(trie_0) == 1
    dict_0 = {}
    var_0 = trie_0.repr_brief(dict_0, dict_0)
    assert var_0 == ""
    str_1 = "m-g"
    var_1 = trie_0.repr_brief(dict_0, str_1)
    assert var_1 == ""
    var_2 = trie_0.__iter__()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "trie.Trie"
    assert len(var_2) == 1
    bool_0 = var_2.__contains__(var_2)
    assert bool_0 is True
    var_3 = trie_0.contains_prefix(dict_0)
    assert var_3 is True
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_4 = var_1.__repr__()
    assert var_4 == "''"
    none_type_1 = trie_0.insert(var_4)
    assert len(trie_0) == 2
    assert len(var_2) == 2
    bool_1 = var_2.__contains__(var_4)
    assert bool_1 is True
    trie_2 = module_0.Trie()
    assert f"{type(trie_2).__module__}.{type(trie_2).__qualname__}" == "trie.Trie"
    assert len(trie_2) == 0
    var_5 = var_1.__iter__()
    var_6 = trie_0.__repr__()
    assert var_6 == "*\n├──c\n└──'\n   └──'"
    trie_3 = module_0.Trie()
    assert f"{type(trie_3).__module__}.{type(trie_3).__qualname__}" == "trie.Trie"
    assert len(trie_3) == 0
    var_7 = trie_0.successors(trie_2)
    var_6.__delitem__(var_5)


@pytest.mark.xfail(strict=True)
def test_case_20():
    trie_0 = module_0.Trie()
    assert f"{type(trie_0).__module__}.{type(trie_0).__qualname__}" == "trie.Trie"
    assert len(trie_0) == 0
    assert (
        f"{type(module_0.logger).__module__}.{type(module_0.logger).__qualname__}"
        == "logging.Logger"
    )
    assert module_0.logger.filters == []
    assert module_0.logger.name == "trie"
    assert module_0.logger.level == 0
    assert (
        f"{type(module_0.logger.parent).__module__}.{type(module_0.logger.parent).__qualname__}"
        == "logging.RootLogger"
    )
    assert module_0.logger.propagate is True
    assert module_0.logger.handlers == []
    assert module_0.logger.disabled is False
    assert (
        f"{type(module_0.logger.manager).__module__}.{type(module_0.logger.manager).__qualname__}"
        == "logging.Manager"
    )
    var_0 = trie_0.generate_recursively(trie_0, trie_0)
    dict_0 = {}
    str_0 = "m-g"
    var_1 = trie_0.repr_brief(dict_0, str_0)
    assert var_1 == ""
    var_2 = trie_0.__iter__()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "trie.Trie"
    assert len(var_2) == 0
    bool_0 = var_2.__contains__(var_2)
    assert bool_0 is False
    var_3 = var_1.__repr__()
    assert var_3 == "''"
    none_type_0 = trie_0.insert(var_3)
    assert len(trie_0) == 1
    assert len(var_2) == 1
    bool_1 = var_2.__contains__(var_3)
    assert bool_1 is True
    var_4 = var_2.__iter__()
    assert f"{type(var_4).__module__}.{type(var_4).__qualname__}" == "trie.Trie"
    assert len(var_4) == 1
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_5 = trie_0.repr_brief(var_1, var_2)
    assert var_5 == ""
    var_6 = trie_0.__repr__()
    assert var_6 == "*\n└──'\n   └──'"
    trie_2 = module_0.Trie()
    assert f"{type(trie_2).__module__}.{type(trie_2).__qualname__}" == "trie.Trie"
    assert len(trie_2) == 0
    str_1 = "#ot1=fyE(bG"
    var_7 = trie_0.successors(trie_1)
    var_8 = trie_1.repr_brief(trie_0, str_1)
    assert var_8 == "''"
    none_type_1 = var_2.insert(var_7)
    assert len(trie_0) == 2
    assert len(var_2) == 2
    assert len(var_4) == 2
    var_9 = var_2.__delitem__(var_3)
    assert len(trie_0) == 1
    assert len(var_2) == 1
    assert len(var_4) == 1
    set_0 = {var_8}
    trie_1.delete_recursively(trie_1, set_0)
