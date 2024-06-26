# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bst as module_0
import typing as module_1


def test_case_0():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    bool_0 = False
    none_type_0 = None
    list_0 = [none_type_0]
    var_0 = binary_search_tree_0.iterate_leaves()
    tuple_0 = (list_0, var_0, var_0, var_0)
    generator_0 = binary_search_tree_0.get_nodes_in_range_inclusive(bool_0, tuple_0)
    none_type_1 = binary_search_tree_0.insert(binary_search_tree_0)
    assert len(binary_search_tree_0) == 1
    var_1 = binary_search_tree_0.iterate_inorder()
    binary_search_tree_0.parent_path(var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    protocol_0 = module_1.Protocol()
    assert (
        f"{type(protocol_0).__module__}.{type(protocol_0).__qualname__}"
        == "typing.Protocol"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
    bool_0 = binary_search_tree_0.__delitem__(protocol_0)
    assert bool_0 is False
    none_type_0 = None
    str_0 = "_!D@6*`"
    var_0 = binary_search_tree_0.get_root()
    str_1 = binary_search_tree_0.repr_traverse(
        none_type_0, str_0, none_type_0, none_type_0
    )
    assert str_1 == ""
    str_2 = 'O><ny$M^D,7TS"I+,='
    str_3 = "__main__"
    tuple_0 = (str_2, str_3)
    var_1 = binary_search_tree_0.get_root()
    node_0 = module_0.Node(str_3)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert node_0.value == "__main__"
    bool_1 = binary_search_tree_0.iterate_inorder()
    node_1 = module_0.Node(tuple_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "bst.Node"
    assert node_1.left is None
    assert node_1.right is None
    assert node_1.value == ('O><ny$M^D,7TS"I+,=', "__main__")
    none_type_1 = binary_search_tree_0.insert(node_0)
    assert len(binary_search_tree_0) == 1
    binary_search_tree_0.__getitem__(binary_search_tree_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    node_0 = module_0.Node(bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert node_0.value is True
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    binary_search_tree_1 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_1).__module__}.{type(binary_search_tree_1).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_1) == 0
    bool_1 = binary_search_tree_1.__contains__(bool_0)
    assert bool_1 is False
    dict_0 = {binary_search_tree_0: binary_search_tree_0, bool_0: node_0}
    node_1 = module_0.Node(dict_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "bst.Node"
    assert node_1.left is None
    assert node_1.right is None
    assert (
        f"{type(node_1.value).__module__}.{type(node_1.value).__qualname__}"
        == "builtins.dict"
    )
    assert len(node_1.value) == 2
    none_type_0 = binary_search_tree_1.insert(dict_0)
    assert len(binary_search_tree_1) == 1
    var_0 = binary_search_tree_1.iterate_postorder()
    var_0.__getitem__(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    bool_0 = False
    none_type_0 = None
    list_0 = [none_type_0]
    var_0 = binary_search_tree_0.iterate_leaves()
    tuple_0 = (list_0, var_0, var_0, var_0)
    generator_0 = binary_search_tree_0.get_nodes_in_range_inclusive(bool_0, tuple_0)
    none_type_1 = var_0.__repr__()
    var_1 = binary_search_tree_0.iterate_inorder()
    list_1 = binary_search_tree_0.parent_path(var_1)
    var_1.height()


@pytest.mark.xfail(strict=True)
def test_case_5():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    binary_search_tree_1 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_1).__module__}.{type(binary_search_tree_1).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_1) == 0
    var_0 = binary_search_tree_1.iterate_leaves()
    var_1 = binary_search_tree_1.iterate_leaves()
    bool_0 = binary_search_tree_1.__delitem__(var_1)
    assert bool_0 is False
    var_1.iterate_preorder()


def test_case_6():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    int_0 = binary_search_tree_0.height()
    assert int_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_7():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    protocol_0 = module_1.Protocol()
    assert (
        f"{type(protocol_0).__module__}.{type(protocol_0).__qualname__}"
        == "typing.Protocol"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
    bool_0 = binary_search_tree_0.__delitem__(protocol_0)
    assert bool_0 is False
    none_type_0 = None
    none_type_1 = binary_search_tree_0.insert(none_type_0)
    assert len(binary_search_tree_0) == 1
    str_0 = "_!D@6*`"
    var_0 = binary_search_tree_0.get_root()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "bst.Node"
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.value is None
    str_1 = binary_search_tree_0.repr_traverse(
        none_type_0, str_0, none_type_0, none_type_0
    )
    assert str_1 == ""
    str_2 = "__main__"
    var_1 = binary_search_tree_0.get_root()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "bst.Node"
    assert var_1.left is None
    assert var_1.right is None
    assert var_1.value is None
    node_0 = module_0.Node(str_2)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert node_0.value == "__main__"
    binary_search_tree_0.insert(node_0)


def test_case_8():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    int_0 = binary_search_tree_0.__repr__()
    assert int_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_9():
    bool_0 = True
    node_0 = module_0.Node(bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert node_0.value is True
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.iterate_inorder()
    var_0.iterate_postorder()


@pytest.mark.xfail(strict=True)
def test_case_10():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.get_root()
    list_0 = binary_search_tree_0.parent_path(var_0)
    var_1 = binary_search_tree_0.__len__()
    assert var_1 == 0
    var_1.iterate_postorder()


@pytest.mark.xfail(strict=True)
def test_case_11():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.__len__()
    assert var_0 == 0
    var_0.iterate_leaves()


@pytest.mark.xfail(strict=True)
def test_case_12():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.iterate_leaves()
    float_0 = 3272.76527
    none_type_0 = binary_search_tree_0.insert(float_0)
    assert len(binary_search_tree_0) == 1
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 1
    binary_search_tree_0.get_next_node(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    protocol_0 = module_1.Protocol()
    assert (
        f"{type(protocol_0).__module__}.{type(protocol_0).__qualname__}"
        == "typing.Protocol"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
    none_type_0 = None
    str_0 = "_!D@6*`"
    var_0 = binary_search_tree_0.get_root()
    str_1 = binary_search_tree_0.repr_traverse(
        none_type_0, str_0, none_type_0, none_type_0
    )
    assert str_1 == ""
    str_2 = "__main__"
    var_1 = binary_search_tree_0.iterate_postorder()
    var_2 = binary_search_tree_0.get_root()
    node_0 = module_0.Node(str_2)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert node_0.value == "__main__"
    var_3 = binary_search_tree_0.iterate_inorder()
    str_3 = ""
    binary_search_tree_0.repr_traverse(str_1, str_3, var_3, var_1)


@pytest.mark.xfail(strict=True)
def test_case_14():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    protocol_0 = module_1.Protocol()
    assert (
        f"{type(protocol_0).__module__}.{type(protocol_0).__qualname__}"
        == "typing.Protocol"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
    none_type_0 = None
    none_type_1 = binary_search_tree_0.insert(none_type_0)
    assert len(binary_search_tree_0) == 1
    str_0 = "_!D@6*`"
    var_0 = binary_search_tree_0.get_root()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "bst.Node"
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.value is None
    str_1 = binary_search_tree_0.repr_traverse(
        none_type_0, str_0, none_type_0, none_type_0
    )
    assert str_1 == ""
    var_1 = binary_search_tree_0.__getitem__(none_type_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "bst.Node"
    assert var_1.left is None
    assert var_1.right is None
    assert var_1.value is None
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 1
    str_2 = "__main__"
    tuple_0 = binary_search_tree_0.iterate_preorder()
    var_2 = binary_search_tree_0.get_root()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "bst.Node"
    assert var_2.left is None
    assert var_2.right is None
    assert var_2.value is None
    node_0 = module_0.Node(str_2)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert node_0.value == "__main__"
    binary_search_tree_0.__contains__(node_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    none_type_0 = None
    none_type_1 = binary_search_tree_0.insert(none_type_0)
    assert len(binary_search_tree_0) == 1
    var_0 = binary_search_tree_0.__repr__()
    assert var_0 == "None"
    int_0 = binary_search_tree_0.height()
    assert int_0 == 1
    var_1 = binary_search_tree_0.iterate_inorder()
    var_2 = binary_search_tree_0.iterate_inorder()
    binary_search_tree_0.parent_path(var_2)


@pytest.mark.xfail(strict=True)
def test_case_16():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    protocol_0 = module_1.Protocol()
    assert (
        f"{type(protocol_0).__module__}.{type(protocol_0).__qualname__}"
        == "typing.Protocol"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
    list_0 = binary_search_tree_0.parent_path(protocol_0)
    none_type_0 = None
    none_type_1 = binary_search_tree_0.insert(none_type_0)
    assert len(binary_search_tree_0) == 1
    var_0 = binary_search_tree_0.__getitem__(none_type_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "bst.Node"
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.value is None
    var_1 = binary_search_tree_0.get_next_node(var_0)
    bool_0 = binary_search_tree_0.__delitem__(none_type_0)
    assert bool_0 is True
    assert len(binary_search_tree_0) == 0
    var_2 = binary_search_tree_0.iterate_inorder()
    var_2.iterate_inorder()


@pytest.mark.xfail(strict=True)
def test_case_17():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    protocol_0 = module_1.Protocol()
    assert (
        f"{type(protocol_0).__module__}.{type(protocol_0).__qualname__}"
        == "typing.Protocol"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
    bool_0 = binary_search_tree_0.__delitem__(protocol_0)
    assert bool_0 is False
    none_type_0 = None
    none_type_1 = binary_search_tree_0.insert(none_type_0)
    assert len(binary_search_tree_0) == 1
    var_0 = binary_search_tree_0.__getitem__(none_type_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "bst.Node"
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.value is None
    int_0 = binary_search_tree_0.height()
    assert int_0 == 1
    binary_search_tree_0.__delitem__(bool_0)


def test_case_18():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    protocol_0 = module_1.Protocol()
    assert (
        f"{type(protocol_0).__module__}.{type(protocol_0).__qualname__}"
        == "typing.Protocol"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
    bool_0 = binary_search_tree_0.__delitem__(protocol_0)
    assert bool_0 is False
    none_type_0 = None
    none_type_1 = None
    none_type_2 = binary_search_tree_0.insert(none_type_1)
    assert len(binary_search_tree_0) == 1
    var_0 = binary_search_tree_0.__getitem__(none_type_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "bst.Node"
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.value is None
    str_0 = "_!D@6*`"
    str_1 = binary_search_tree_0.repr_traverse(
        none_type_0, str_0, none_type_0, none_type_0
    )
    assert str_1 == ""
    var_1 = binary_search_tree_0.__len__()
    assert var_1 == 1
    binary_search_tree_1 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_1).__module__}.{type(binary_search_tree_1).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_1) == 0
    with pytest.raises(AssertionError):
        binary_search_tree_1.get_next_node(var_0)


@pytest.mark.xfail(strict=True)
def test_case_19():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    protocol_0 = module_1.Protocol()
    assert (
        f"{type(protocol_0).__module__}.{type(protocol_0).__qualname__}"
        == "typing.Protocol"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
    list_0 = binary_search_tree_0.parent_path(protocol_0)
    none_type_0 = None
    none_type_1 = binary_search_tree_0.insert(none_type_0)
    assert len(binary_search_tree_0) == 1
    list_1 = []
    node_0 = module_0.Node(list_1)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert node_0.value == []
    binary_search_tree_0.get_next_node(node_0)


def test_case_20():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    protocol_0 = module_1.Protocol()
    assert (
        f"{type(protocol_0).__module__}.{type(protocol_0).__qualname__}"
        == "typing.Protocol"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
    list_0 = binary_search_tree_0.parent_path(protocol_0)
    none_type_0 = None
    none_type_1 = binary_search_tree_0.insert(none_type_0)
    assert len(binary_search_tree_0) == 1
    var_0 = module_0.Node(none_type_1)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "bst.Node"
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.value is None
    str_0 = "_!D@6*`"
    str_1 = binary_search_tree_0.repr_traverse(
        none_type_0, str_0, none_type_0, none_type_0
    )
    assert str_1 == ""
    var_1 = binary_search_tree_0.__repr__()
    assert var_1 == "None"
    int_0 = binary_search_tree_0.height()
    assert int_0 == 1
    with pytest.raises(AssertionError):
        binary_search_tree_0.get_next_node(var_0)


@pytest.mark.xfail(strict=True)
def test_case_21():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    protocol_0 = module_1.Protocol()
    assert (
        f"{type(protocol_0).__module__}.{type(protocol_0).__qualname__}"
        == "typing.Protocol"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
    list_0 = binary_search_tree_0.parent_path(protocol_0)
    none_type_0 = None
    none_type_1 = binary_search_tree_0.insert(none_type_0)
    assert len(binary_search_tree_0) == 1
    var_0 = binary_search_tree_0.__getitem__(none_type_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "bst.Node"
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.value is None
    str_0 = "_!D@6*`"
    binary_search_tree_0.repr_traverse(none_type_0, str_0, var_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_22():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    protocol_0 = module_1.Protocol()
    assert (
        f"{type(protocol_0).__module__}.{type(protocol_0).__qualname__}"
        == "typing.Protocol"
    )
    assert module_1.EXCLUDED_ATTRIBUTES == [
        "__parameters__",
        "__orig_bases__",
        "__orig_class__",
        "_is_protocol",
        "_is_runtime_protocol",
        "__abstractmethods__",
        "__annotations__",
        "__dict__",
        "__doc__",
        "__init__",
        "__module__",
        "__new__",
        "__slots__",
        "__subclasshook__",
        "__weakref__",
        "__class_getitem__",
        "_MutableMapping__marker",
    ]
    assert (
        f"{type(module_1.T).__module__}.{type(module_1.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.KT).__module__}.{type(module_1.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT).__module__}.{type(module_1.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_co).__module__}.{type(module_1.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.V_co).__module__}.{type(module_1.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.VT_co).__module__}.{type(module_1.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.T_contra).__module__}.{type(module_1.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.CT_co).__module__}.{type(module_1.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_1.AnyStr).__module__}.{type(module_1.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_1.TYPE_CHECKING is False
    list_0 = binary_search_tree_0.parent_path(protocol_0)
    var_0 = binary_search_tree_0.get_root()
    none_type_0 = binary_search_tree_0.insert(var_0)
    assert len(binary_search_tree_0) == 1
    var_1 = binary_search_tree_0.__getitem__(none_type_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "bst.Node"
    assert var_1.left is None
    assert var_1.right is None
    assert var_1.value is None
    str_0 = "_!D@6*`"
    binary_search_tree_0.repr_traverse(var_1, str_0, var_1, var_1)
