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
    str_0 = "U#Fi9TeQ3\x0bL @`*C"
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
    none_type_0 = trie_0.insert(str_0)
    assert len(trie_0) == 1
    var_0 = trie_0.__repr__()
    assert (
        var_0
        == "*\n└──U\n   └──#\n      └──F\n         └──i\n            └──9\n               └──T\n                  └──e\n                     └──Q\n                        └──3\n                           └──\x0b\n                              └──L\n                                 └── \n                                    └──@\n                                       └──`\n                                          └──*\n                                             └──C"
    )
    var_1 = var_0.__repr__()
    assert (
        var_1
        == "'*\\n└──U\\n   └──#\\n      └──F\\n         └──i\\n            └──9\\n               └──T\\n                  └──e\\n                     └──Q\\n                        └──3\\n                           └──\\x0b\\n                              └──L\\n                                 └── \\n                                    └──@\\n                                       └──`\\n                                          └──*\\n                                             └──C'"
    )


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
    var_0 = trie_0.successors(trie_0)
    str_0 = "of5=c^LI\x0b3"
    none_type_0 = trie_0.insert(str_0)
    assert len(trie_0) == 1
    var_1 = trie_0.repr_brief(trie_0, var_0)
    assert var_1 == "of5=c^LI\x0b3"
    var_2 = trie_0.__repr__()
    assert (
        var_2
        == "*\n└──o\n   └──f\n      └──5\n         └──=\n            └──c\n               └──^\n                  └──L\n                     └──I\n                        └──\x0b\n                           └──3"
    )
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    bool_0 = trie_0.__contains__(var_1)
    assert bool_0 is True
    var_3 = trie_0.generate_recursively(var_1, var_1)
    dict_0 = {var_2: trie_1}
    var_4 = dict_0.__repr__()
    assert (
        var_4
        == "{'*\\n└──o\\n   └──f\\n      └──5\\n         └──=\\n            └──c\\n               └──^\\n                  └──L\\n                     └──I\\n                        └──\\x0b\\n                           └──3': *}"
    )
    with pytest.raises(KeyError):
        trie_1.__delitem__(var_2)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '"R>q=\\$Ene'
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
    var_0 = trie_0.successors(str_0)
    var_0.__next__()


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
    str_0 = "mHQ_{mI.@{X-B\nY<"
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
        trie_0.__getitem__(str_0)


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
    dict_0 = {}
    trie_0.delete_recursively(dict_0, var_0)


@pytest.mark.xfail(strict=True)
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
    trie_0.delete_recursively(trie_0, trie_0)


def test_case_8():
    str_0 = "U#Fi9TeQ3\x0bL C@`*C"
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
    none_type_0 = trie_0.insert(str_0)
    assert len(trie_0) == 1
    var_0 = trie_0.successors(trie_0)
    var_1 = trie_0.__repr__()
    assert (
        var_1
        == "*\n└──U\n   └──#\n      └──F\n         └──i\n            └──9\n               └──T\n                  └──e\n                     └──Q\n                        └──3\n                           └──\x0b\n                              └──L\n                                 └── \n                                    └──C\n                                       └──@\n                                          └──`\n                                             └──*\n                                                └──C"
    )


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
    bool_0 = trie_0.successors(trie_0)
    var_0 = trie_0.contains_prefix(bool_0)
    assert var_0 is True
    var_1 = trie_0.__traverse__(trie_0)


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
    var_0 = trie_0.__repr__()
    assert var_0 == "*"
    var_1 = trie_0.successors(trie_0)
    str_0 = "pA-4"
    trie_0.repr_brief(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    dict_0 = {}
    str_0 = 'nZcH2S(#")@|m Lcn+&%'
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
    var_0 = trie_0.repr_brief(dict_0, str_0)
    assert var_0 == ""
    var_1 = var_0.__repr__()
    assert var_1 == "''"
    var_0.insert(var_0)


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
    var_0 = trie_0.contains_prefix(trie_0)
    assert var_0 is True


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
    var_0 = trie_0.__len__()
    assert var_0 == 0


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
    none_type_0 = None
    str_0 = "of5=c^LI\x0b3"
    none_type_1 = trie_0.insert(str_0)
    assert len(trie_0) == 1
    var_0 = trie_0.repr_brief(trie_0, none_type_0)
    assert var_0 == "of5=c^LI\x0b3"
    bool_0 = trie_0.__contains__(var_0)
    assert bool_0 is True
    var_1 = trie_0.generate_recursively(var_0, var_0)
    var_2 = var_0.__repr__()
    assert var_2 == "'of5=c^LI\\x0b3'"
    var_3 = var_1.__repr__()
    var_4 = trie_0.__delitem__(var_0)
    assert len(trie_0) == 0


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
    dict_0 = {var_0: var_0}
    bool_0 = trie_0.delete_recursively(dict_0, var_0)
    assert bool_0 is True
    var_1 = trie_0.__traverse__(trie_0)


@pytest.mark.xfail(strict=True)
def test_case_17():
    str_0 = "U#Fi9TeQ3\x0bL @`*C"
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
    dict_0 = {trie_0: trie_0}
    str_1 = "4qF=T\\|~{RR"
    none_type_0 = trie_0.insert(str_0)
    assert len(trie_0) == 1
    var_0 = trie_0.repr_brief(dict_0, str_1)
    assert (
        var_0
        == "*\n└──U\n   └──#\n      └──F\n         └──i\n            └──9\n               └──T\n                  └──e\n                     └──Q\n                        └──3\n                           └──\x0b\n                              └──L\n                                 └── \n                                    └──@\n                                       └──`\n                                          └──*\n                                             └──C4qF=T\\|~{RRU#Fi9TeQ3\x0bL @`*C"
    )
    none_type_1 = None
    var_1 = trie_0.repr_brief(trie_0, none_type_1)
    assert var_1 == "U#Fi9TeQ3\x0bL @`*C"
    var_2 = trie_0.__len__()
    assert var_2 == 1
    var_3 = trie_0.contains_prefix(var_1)
    assert var_3 is True
    var_4 = trie_0.successors(str_0)
    bool_0 = True
    var_0.delete_recursively(bool_0, var_0)


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
    none_type_0 = None
    var_0 = trie_0.repr_brief(trie_0, none_type_0)
    assert var_0 == ""
    var_1 = trie_0.contains_prefix(var_0)
    assert var_1 is True
    var_2 = trie_0.successors(var_0)
    var_3 = trie_0.__repr__()
    assert var_3 == "*"
    var_4 = trie_0.successors(trie_0)
    dict_0 = {var_3: var_0, var_0: var_0}
    var_5 = var_4.__iter__()
    var_6 = trie_0.repr_brief(dict_0, var_1)
    assert var_6 == "[*,]"
    bool_0 = trie_0.delete_recursively(dict_0, var_3)
    assert bool_0 is False
    var_3.__delitem__(dict_0)


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
    var_0 = trie_0.successors(trie_0)
    none_type_0 = None
    str_0 = "__main__"
    none_type_1 = trie_0.insert(str_0)
    assert len(trie_0) == 1
    var_1 = trie_0.repr_brief(trie_0, none_type_0)
    assert var_1 == "__main__"
    var_2 = trie_0.successors(var_0)
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_3 = trie_0.successors(trie_0)
    bool_0 = trie_0.__contains__(var_1)
    assert bool_0 is True
    var_4 = trie_0.generate_recursively(var_1, var_1)


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
    var_0 = trie_0.successors(trie_0)
    none_type_0 = None
    str_0 = "U"
    none_type_1 = trie_0.insert(str_0)
    assert len(trie_0) == 1
    var_1 = trie_0.repr_brief(trie_0, none_type_0)
    assert var_1 == "U"
    var_2 = trie_0.__repr__()
    assert var_2 == "*\n└──U"
    trie_1 = module_0.Trie()
    assert f"{type(trie_1).__module__}.{type(trie_1).__qualname__}" == "trie.Trie"
    assert len(trie_1) == 0
    var_3 = trie_0.successors(trie_0)
    bool_0 = trie_0.__contains__(var_1)
    assert bool_0 is True
    var_4 = trie_0.generate_recursively(var_1, var_1)
    dict_0 = {var_2: var_3}
    var_5 = dict_0.__repr__()
    assert var_5 == "{'*\\n└──U': []}"
    dict_1 = {none_type_0: var_0}
    trie_0.delete_recursively(dict_1, trie_0)
