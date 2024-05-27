# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import trie as module_0


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


def test_case_1():
    str_0 = "*c(;V6G4"
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
    var_0 = trie_0.__iter__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "trie.Trie"
    assert len(var_0) == 0
    with pytest.raises(KeyError):
        trie_0.__delitem__(str_0)


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
    dict_0 = trie_0.__getitem__(trie_0)
    bool_0 = trie_0.__contains__(trie_0)
    assert bool_0 is False


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
    dict_0 = trie_0.__getitem__(trie_0)


@pytest.mark.xfail(strict=True)
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
    trie_0.delete_recursively(trie_0, trie_0)


def test_case_5():
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
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    var_1 = trie_0.successors(var_0)
    none_type_1 = trie_0.insert(trie_0)
    assert len(trie_0) == 2
    var_2 = trie_0.__iter__()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "trie.Trie"
    assert len(var_2) == 2
    var_3 = var_2.__repr__()
    assert var_3 == "*\n└──*"
    var_4 = trie_0.__iter__()
    assert f"{type(var_4).__module__}.{type(var_4).__qualname__}" == "trie.Trie"
    assert len(var_4) == 2
    var_5 = var_4.successors(var_3)
    var_6 = trie_0.generate_recursively(trie_0, var_5)
    trie_0.__delitem__(var_2)


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


def test_case_8():
    bool_0 = True
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
    var_0 = trie_0.__iter__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "trie.Trie"
    assert len(var_0) == 0
    dict_0 = {bool_0: trie_0, trie_0: trie_0}
    var_1 = trie_0.repr_brief(dict_0, bool_0)
    assert var_1 == "[True,*]"


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
    dict_0 = trie_0.__repr__()
    assert dict_0 == "*"
    bool_0 = trie_0.repr_brief(trie_0, trie_0)
    assert bool_0 == ""


@pytest.mark.xfail(strict=True)
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
    var_0 = trie_0.contains_prefix(trie_0)
    assert var_0 is True
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_1 = trie_1.__len__()
    assert var_1 == 0
    var_2 = trie_1.__len__()
    assert var_2 == 0
    var_2.__len__()


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
    var_0 = trie_0.successors(trie_0)
    with pytest.raises(KeyError):
        trie_0.__delitem__(trie_0)


@pytest.mark.xfail(strict=True)
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
    none_type_0 = trie_0.insert(trie_0)
    assert len(trie_0) == 1
    trie_0.insert(trie_0)


@pytest.mark.xfail(strict=True)
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
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    var_1 = trie_0.successors(var_0)
    bool_0 = trie_0.delete_recursively(trie_0, var_0)
    assert bool_0 is True
    assert len(trie_0) == 0
    var_1.repr_brief(var_1, var_0)


@pytest.mark.xfail(strict=True)
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
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    none_type_1 = trie_0.insert(trie_0)
    assert len(trie_0) == 2
    var_1 = trie_0.__iter__()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "trie.Trie"
    assert len(var_1) == 2
    bytes_0 = b"\xff\xd2\x1d#@\x10\xc9U\xf2\xd2\xbb\x13}\x05"
    var_2 = var_1.__repr__()
    assert var_2 == "*\n└──*"
    bytes_0.successors(var_2)


@pytest.mark.xfail(strict=True)
def test_case_15():
    bool_0 = True
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
    none_type_1 = trie_0.insert(trie_0)
    assert len(trie_0) == 2
    bytes_0 = b"\xff\xd2\x1d#@\x10\xc9U\xf2\xd2\xbb\x13}\x05"
    var_1 = bool_0.__repr__()
    assert var_1 == "True"
    bytes_0.successors(var_1)


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
    none_type_0 = trie_0.insert(trie_0)
    assert len(trie_0) == 1
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_0 = trie_0.__traverse__(trie_1)
    with pytest.raises(KeyError):
        trie_0.__getitem__(trie_0)


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
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    var_1 = trie_0.successors(var_0)
    bool_0 = trie_0.delete_recursively(trie_0, var_0)
    assert bool_0 is True
    assert len(trie_0) == 0
    none_type_1 = trie_0.insert(trie_0)
    assert len(trie_0) == 1
    var_2 = trie_0.__iter__()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "trie.Trie"
    assert len(var_2) == 1
    bool_1 = trie_0.__contains__(var_1)
    assert bool_1 is True
    var_3 = var_2.__repr__()
    assert var_3 == "*"
    var_4 = trie_0.repr_brief(trie_0, none_type_0)
    assert var_4 == ","
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    with pytest.raises(KeyError):
        var_2.__delitem__(var_0)


@pytest.mark.xfail(strict=True)
def test_case_18():
    bool_0 = True
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
    dict_0 = {bool_0: trie_0, trie_0: trie_0}
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    trie_0.repr_brief(dict_0, bool_0)


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
    var_0 = trie_0.__traverse__(trie_0)
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    var_1 = trie_0.successors(var_0)
    trie_0.insert(trie_0)


@pytest.mark.xfail(strict=True)
def test_case_20():
    bool_0 = True
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
    dict_0 = {bool_0: trie_0, trie_0: trie_0}
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    var_1 = trie_0.successors(dict_0)
    none_type_1 = trie_0.insert(dict_0)
    assert len(trie_0) == 2
    var_2 = trie_0.__iter__()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "trie.Trie"
    assert len(var_2) == 2
    bool_1 = trie_0.__contains__(dict_0)
    assert bool_1 is True
    trie_0.__repr__()


@pytest.mark.xfail(strict=True)
def test_case_21():
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
    var_1 = trie_0.successors(var_0)
    var_2 = var_1.__repr__()
    assert var_2 == "[]"
    var_3 = trie_0.__iter__()
    assert f"{type(var_3).__module__}.{type(var_3).__qualname__}" == "trie.Trie"
    assert len(var_3) == 1
    none_type_1 = trie_0.insert(var_2)
    assert len(trie_0) == 2
    assert len(var_3) == 2
    var_4 = var_3.__delitem__(var_2)
    assert len(trie_0) == 1
    assert len(var_3) == 1
    bool_0 = var_2.__iter__()
    var_5 = var_1.__repr__()
    assert var_5 == "[]"
    var_4.repr_brief(trie_0, var_1)