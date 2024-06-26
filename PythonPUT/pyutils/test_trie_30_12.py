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
    none_type_0 = trie_0.insert(trie_0)
    assert len(trie_0) == 1
    var_0 = trie_0.repr_brief(trie_0, trie_0)
    assert var_0 == ","
    var_1 = trie_0.generate_recursively(none_type_0, none_type_0)
    var_1.generate_recursively(var_0, var_1)


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
    var_0 = trie_0.successors(trie_0)
    var_1 = trie_0.__iter__()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "trie.Trie"
    assert len(var_1) == 1
    str_0 = "_h$5_-}:Vo[x'l~Q\\"
    with pytest.raises(KeyError):
        var_1.__delitem__(str_0)


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
    var_0 = trie_0.__iter__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "trie.Trie"
    assert len(var_0) == 0
    var_1 = var_0.__traverse__(trie_0)
    with pytest.raises(KeyError):
        var_0.__delitem__(var_1)


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
    var_0 = module_0.Trie()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "trie.Trie"
    assert len(var_0) == 0
    var_1 = var_0.contains_prefix(trie_0)
    assert var_1 is True


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
    var_0 = trie_0.__repr__()
    assert var_0 == "*"


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
    var_0 = trie_0.__iter__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "trie.Trie"
    assert len(var_0) == 0
    var_1 = var_0.__len__()
    assert var_1 == 0
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    trie_1.successors(var_1)


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
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_0 = trie_1.__iter__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "trie.Trie"
    assert len(var_0) == 0


def test_case_8():
    bytes_0 = b"\xd1}\r\xadw\xd9\xbd^r"
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
        trie_0.__getitem__(bytes_0)


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
    var_0 = trie_0.successors(trie_0)
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    var_1 = trie_0.repr_brief(trie_0, trie_0)
    assert var_1 == ","
    str_0 = "_h$5_-}:co[x'l~Q\\#"
    var_2 = trie_0.repr_brief(var_0, var_0)
    assert var_2 == ""
    var_3 = trie_0.repr_brief(var_0, str_0)
    assert var_3 == ""
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_4 = trie_1.generate_recursively(var_3, var_3)
    none_type_0.generate_recursively(var_2, var_4)


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
    trie_0.delete_recursively(trie_0, trie_0)


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
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    none_type_0 = var_0.__repr__()
    var_1 = trie_0.successors(var_0)
    var_2 = trie_0.__iter__()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "trie.Trie"
    assert len(var_2) == 0
    dict_0 = {var_2: var_2}
    str_0 = "_h$5_-}:Vo[x'l~Q\\"
    none_type_1 = trie_0.insert(str_0)
    assert len(trie_0) == 1
    assert len(var_2) == 1
    var_3 = trie_0.repr_brief(dict_0, str_0)
    assert (
        var_3
        == "*\n└──_\n   └──h\n      └──$\n         └──5\n            └──_\n               └──-\n                  └──}\n                     └──:\n                        └──V\n                           └──o\n                              └──[\n                                 └──x\n                                    └──'\n                                       └──l\n                                          └──~\n                                             └──Q\n                                                └──\\_h$5_-}:Vo[x'l~Q\\_h$5_-}:Vo[x'l~Q\\"
    )
    var_4 = var_2.__delitem__(str_0)
    assert len(trie_0) == 0
    assert len(var_2) == 0


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
    var_0 = trie_0.successors(trie_0)
    var_1 = trie_0.__iter__()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "trie.Trie"
    assert len(var_1) == 1
    str_0 = "_h$5_-}:Vo[x'l~Q\\"
    none_type_1 = trie_0.insert(str_0)
    assert len(trie_0) == 2
    assert len(var_1) == 2
    var_2 = var_1.__delitem__(str_0)
    assert len(trie_0) == 1
    assert len(var_1) == 1


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
    none_type_0 = trie_0.insert(trie_0)
    assert len(trie_0) == 1
    var_0 = trie_0.__iter__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "trie.Trie"
    assert len(var_0) == 1
    var_1 = trie_0.repr_brief(var_0, var_0)
    assert var_1 == ","
    with pytest.raises(KeyError):
        var_0.__delitem__(var_0)


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
    var_1 = trie_0.successors(var_0)
    var_2 = trie_0.repr_brief(trie_0, trie_0)
    assert var_2 == "*"
    var_3 = trie_0.__iter__()
    assert f"{type(var_3).__module__}.{type(var_3).__qualname__}" == "trie.Trie"
    assert len(var_3) == 1
    dict_0 = {var_3: var_3}
    str_0 = "_h$5_-}:Vo[x'l~Q\\"
    none_type_1 = trie_0.insert(str_0)
    assert len(trie_0) == 2
    assert len(var_3) == 2
    var_4 = trie_0.repr_brief(dict_0, str_0)
    assert (
        var_4
        == "*\n├──*\n└──_\n   └──h\n      └──$\n         └──5\n            └──_\n               └──-\n                  └──}\n                     └──:\n                        └──V\n                           └──o\n                              └──[\n                                 └──x\n                                    └──'\n                                       └──l\n                                          └──~\n                                             └──Q\n                                                └──\\_h$5_-}:Vo[x'l~Q\\[*,_h$5_-}:Vo[x'l~Q\\]"
    )
    var_5 = var_3.__delitem__(str_0)
    assert len(trie_0) == 1
    assert len(var_3) == 1


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
    var_0 = trie_0.successors(trie_0)
    none_type_0 = trie_0.insert(var_0)
    assert len(trie_0) == 1
    var_1 = trie_0.__len__()
    assert var_1 == 1
    var_2 = trie_0.__iter__()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "trie.Trie"
    assert len(var_2) == 1
    dict_0 = {var_2: var_2}
    str_0 = "_h$5_-}:co[x'l~Q\\#"
    none_type_1 = trie_0.insert(str_0)
    assert len(trie_0) == 2
    assert len(var_2) == 2
    var_3 = trie_0.repr_brief(var_0, var_0)
    assert var_3 == ""
    var_4 = trie_0.repr_brief(dict_0, str_0)
    assert (
        var_4
        == "*\n└──_\n   └──h\n      └──$\n         └──5\n            └──_\n               └──-\n                  └──}\n                     └──:\n                        └──c\n                           └──o\n                              └──[\n                                 └──x\n                                    └──'\n                                       └──l\n                                          └──~\n                                             └──Q\n                                                └──\\\n                                                   └──#_h$5_-}:co[x'l~Q\\#[_h$5_-}:co[x'l~Q\\#__h$5_-}:co[x'l~Q\\#h_h$5_-}:co[x'l~Q\\#$_h$5_-}:co[x'l~Q\\#5_h$5_-}:co[x'l~Q\\#__h$5_-}:co[x'l~Q\\#-_h$5_-}:co[x'l~Q\\#}_h$5_-}:co[x'l~Q\\#:_h$5_-}:co[x'l~Q\\#c_h$5_-}:co[x'l~Q\\#o_h$5_-}:co[x'l~Q\\#[_h$5_-}:co[x'l~Q\\#x_h$5_-}:co[x'l~Q\\#'_h$5_-}:co[x'l~Q\\#l_h$5_-}:co[x'l~Q\\#~_h$5_-}:co[x'l~Q\\#Q_h$5_-}:co[x'l~Q\\#\\_h$5_-}:co[x'l~Q\\##,_h$5_-}:co[x'l~Q\\#]"
    )
    trie_1 = trie_0.successors(var_0)
    trie_1.generate_recursively(trie_0, var_4)
