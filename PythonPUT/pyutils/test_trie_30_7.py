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
    var_1 = trie_0.__traverse__(var_0)


def test_case_2():
    str_0 = "gAxe"
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
        trie_0.__delitem__(str_0)


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
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    var_1 = trie_0.__len__()
    assert var_1 == 0
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_2 = trie_0.__traverse__(trie_1)
    var_3 = trie_1.repr_brief(var_2, trie_1)
    assert var_3 == ""
    with pytest.raises(KeyError):
        trie_0.__delitem__(var_2)


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
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    var_1 = trie_0.__traverse__(var_0)


def test_case_5():
    none_type_0 = None
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
    dict_0 = {trie_0: none_type_0, none_type_0: none_type_0, trie_0: trie_0}
    with pytest.raises(KeyError):
        trie_0.__getitem__(dict_0)


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
    dict_0 = trie_0.__getitem__(trie_0)
    var_0 = trie_0.__iter__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "trie.Trie"
    assert len(var_0) == 0
    var_0.delete_recursively(var_0, var_0)


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
    var_0 = trie_0.__iter__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "trie.Trie"
    assert len(var_0) == 0
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    assert len(var_0) == 1
    var_1 = trie_0.__traverse__(var_0)


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
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    none_type_0 = trie_0.successors(var_0)
    var_1 = trie_0.__traverse__(var_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    none_type_0 = None
    dict_0 = {}
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
    var_0 = trie_0.successors(dict_0)
    var_0.generate_recursively(none_type_0, none_type_0)


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
    var_0 = trie_0.__repr__()
    assert var_0 == "*"


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
    none_type_0 = trie_0.insert(trie_0)
    assert len(trie_0) == 1
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_0 = trie_0.__iter__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "trie.Trie"
    assert len(var_0) == 1
    var_1 = trie_0.repr_brief(var_0, trie_1)
    assert var_1 == ","
    var_2 = trie_0.__iter__()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "trie.Trie"
    assert len(var_2) == 1
    var_3 = var_2.__repr__()
    assert var_3 == "*"
    var_4 = trie_0.__iter__()
    assert f"{type(var_4).__module__}.{type(var_4).__qualname__}" == "trie.Trie"
    assert len(var_4) == 1
    trie_1.delete_recursively(var_0, trie_0)


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
    dict_0 = {trie_0: trie_0, trie_0: trie_0, trie_0: trie_0}
    var_0 = trie_0.repr_brief(dict_0, trie_0)
    assert var_0 == "*"
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    bool_0 = trie_0.__contains__(var_0)
    assert bool_0 is True
    var_1 = trie_0.__iter__()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "trie.Trie"
    assert len(var_1) == 1
    var_2 = trie_0.__iter__()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "trie.Trie"
    assert len(var_2) == 1
    var_3 = trie_0.__next__()
    assert var_3 == "*"
    var_4 = trie_0.successors(trie_0)
    var_4.repr_brief(var_3, var_2)


@pytest.mark.xfail(strict=True)
def test_case_13():
    str_0 = "G>*Hu{SKP"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
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
    var_0 = trie_0.successors(dict_0)
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    trie_1.contains_prefix(var_0)


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
    var_0 = trie_0.__iter__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "trie.Trie"
    assert len(var_0) == 0
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    assert len(var_0) == 1
    var_1 = trie_0.__traverse__(var_0)
    var_2 = var_0.__len__()
    assert var_2 == 1


@pytest.mark.xfail(strict=True)
def test_case_15():
    int_0 = 4646
    str_0 = "vhKz7mZcc!"
    bool_0 = False
    tuple_0 = (str_0, bool_0, int_0)
    list_0 = []
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
    var_0 = trie_0.generate_recursively(tuple_0, list_0)
    var_0.__next__()


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
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    var_1 = trie_0.__repr__()
    assert var_1 == "*\n└──*"


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
    none_type_0 = None
    list_0 = [trie_0, none_type_0]
    var_0 = trie_0.generate_recursively(none_type_0, list_0)
    dict_0 = {trie_0: trie_0, trie_0: trie_0, trie_0: trie_0, trie_0: trie_0}
    none_type_1 = trie_0.insert(trie_0)
    assert len(trie_0) == 1
    str_0 = "ZkW/H,Uak4@\n|"
    var_1 = trie_0.contains_prefix(str_0)
    assert var_1 is False
    str_1 = "L]!Bg\r2P2"
    bytes_0 = b"\xb93\xb6\xd5\xdb\xcaT\xe5\t"
    var_2 = trie_0.contains_prefix(bytes_0)
    assert var_2 is False
    var_3 = trie_0.repr_brief(dict_0, str_1)
    assert var_3 == "*L]!Bg\r2P2,"
    trie_0.__getitem__(var_1)


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
    dict_0 = {trie_0: trie_0, trie_0: trie_0, trie_0: trie_0}
    var_0 = trie_0.repr_brief(dict_0, trie_0)
    assert var_0 == "*"
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    with pytest.raises(KeyError):
        trie_0.__delitem__(trie_0)


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
    dict_0 = {trie_0: trie_0, trie_0: trie_0, trie_0: trie_0}
    none_type_0 = trie_0.insert(trie_0)
    assert len(trie_0) == 1
    bool_0 = trie_0.delete_recursively(dict_0, trie_0)
    assert bool_0 is True
    with pytest.raises(KeyError):
        trie_0.__delitem__(trie_0)


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
    dict_0 = {trie_0: trie_0, trie_0: trie_0, trie_0: trie_0}
    var_0 = trie_0.repr_brief(dict_0, trie_0)
    assert var_0 == "*"
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    bool_0 = trie_0.__len__()
    assert bool_0 == 1
    var_1 = trie_0.__delitem__(var_0)
    assert len(trie_0) == 0
    bool_1 = var_0.__contains__(var_0)
    assert bool_1 is True
    var_2 = var_0.__iter__()
    var_3 = var_2.__iter__()
    with pytest.raises(StopIteration):
        trie_0.__next__()


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
    dict_0 = {trie_0: trie_0, trie_0: trie_0, trie_0: trie_0}
    list_0 = [trie_0, dict_0]
    var_0 = trie_0.contains_prefix(list_0)
    assert var_0 is False
    var_1 = trie_0.repr_brief(dict_0, trie_0)
    assert var_1 == "*"
    none_type_0 = trie_0.insert(var_1)
    assert len(trie_0) == 1
    bool_0 = trie_0.delete_recursively(dict_0, trie_0)
    assert bool_0 is True
    bool_1 = trie_0.__contains__(dict_0)
    assert bool_1 is False
    var_2 = trie_0.__iter__()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "trie.Trie"
    assert len(var_2) == 1
    var_3 = var_2.successors(dict_0)
    var_4 = var_3.__repr__()
    assert var_4 == "['*']"
    var_5 = trie_0.successors(trie_0)
    var_6 = var_2.__repr__()
    assert var_6 == "*\n└──*"
    var_5.__delitem__(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_22():
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
    dict_0 = {trie_0: trie_0, var_0: var_0, trie_0: trie_0, trie_0: trie_0}
    var_1 = trie_0.__iter__()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "trie.Trie"
    assert len(var_1) == 0
    var_2 = trie_0.repr_brief(dict_0, trie_0)
    none_type_0 = trie_0.insert(var_2)
    assert len(trie_0) == 1
    assert len(var_1) == 1
    bool_0 = trie_0.delete_recursively(dict_0, trie_0)
    assert bool_0 is False
    bool_1 = trie_0.__contains__(dict_0)
    assert bool_1 is False
    var_3 = trie_0.__iter__()
    assert f"{type(var_3).__module__}.{type(var_3).__qualname__}" == "trie.Trie"
    assert len(var_3) == 1
    var_4 = trie_0.__iter__()
    assert f"{type(var_4).__module__}.{type(var_4).__qualname__}" == "trie.Trie"
    assert len(var_4) == 1
    str_0 = 'k{=J4"0/*'
    var_5 = trie_0.repr_brief(trie_0, str_0)
    var_6 = trie_0.successors(trie_0)
    var_7 = var_3.__repr__()
    dict_1 = {}
    var_4.delete_recursively(dict_1, dict_0)


def test_case_23():
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
    dict_0 = {trie_0: trie_0, trie_0: trie_0, trie_0: trie_0}
    var_0 = trie_0.repr_brief(dict_0, trie_0)
    assert var_0 == "*"
    str_0 = "]x6/^h LVbc (#Y|"
    none_type_0 = trie_0.insert(str_0)
    assert len(trie_0) == 1
    none_type_1 = trie_0.insert(var_0)
    assert len(trie_0) == 2
    with pytest.raises(KeyError):
        trie_0.__delitem__(trie_0)