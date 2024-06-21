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
    int_0 = -1832
    int_1 = binary_search_tree_0.depth()
    assert int_1 == 0
    binary_search_tree_1 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_1).__module__}.{type(binary_search_tree_1).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_1) == 0
    none_type_0 = binary_search_tree_1.insert(binary_search_tree_1)
    assert len(binary_search_tree_1) == 1
    binary_search_tree_1.insert(int_0)


def test_case_2():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    node_0 = module_0.Node(binary_search_tree_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert (
        f"{type(node_0.value).__module__}.{type(node_0.value).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(node_0.value) == 0
    with pytest.raises(AssertionError):
        binary_search_tree_0.get_next_node(node_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    bool_0 = binary_search_tree_0.__delitem__(binary_search_tree_0)
    assert bool_0 is False
    none_type_0 = binary_search_tree_0.insert(bool_0)
    assert len(binary_search_tree_0) == 1
    var_0 = binary_search_tree_0.iterate_preorder()
    binary_search_tree_0.get_next_node(var_0)


def test_case_4():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    node_0 = module_0.Node(binary_search_tree_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert (
        f"{type(node_0.value).__module__}.{type(node_0.value).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(node_0.value) == 0
    str_0 = "(MHGo"
    none_type_0 = None
    str_1 = binary_search_tree_0.repr_traverse(str_0, str_0, node_0, none_type_0)
    assert str_1 == "\n(MHGo(MHGo"
    var_0 = binary_search_tree_0.iterate_postorder()


@pytest.mark.xfail(strict=True)
def test_case_5():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.__repr__()
    assert var_0 == ""
    var_0.depth()


def test_case_6():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.get_root()
    bool_0 = binary_search_tree_0.__delitem__(var_0)
    assert bool_0 is False
    var_1 = binary_search_tree_0.iterate_postorder()
    var_2 = var_0.__repr__()
    assert var_2 == "None"
    var_3 = binary_search_tree_0.__repr__()
    assert var_3 == ""
    var_4 = binary_search_tree_0.iterate_leaves()
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 0
    node_0 = module_0.Node(binary_search_tree_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert (
        f"{type(node_0.value).__module__}.{type(node_0.value).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(node_0.value) == 0
    generator_0 = binary_search_tree_0.iterate_nodes_by_depth(binary_search_tree_0)
    none_type_0 = binary_search_tree_0.insert(binary_search_tree_0)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    with pytest.raises(AssertionError):
        binary_search_tree_0.get_next_node(node_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.__len__()
    assert var_0 == 0
    var_0.iterate_inorder()


def test_case_8():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    node_0 = module_0.Node(binary_search_tree_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert (
        f"{type(node_0.value).__module__}.{type(node_0.value).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(node_0.value) == 0
    none_type_0 = None
    var_0 = binary_search_tree_0.__getitem__(none_type_0)
    var_1 = binary_search_tree_0.__repr__()
    assert var_1 == ""
    int_0 = binary_search_tree_0.height()
    assert int_0 == 0
    var_2 = var_1.__repr__()
    assert var_2 == "''"
    var_3 = var_2.__len__()
    assert var_3 == 2
    var_4 = var_2.__getitem__(int_0)
    assert var_4 == "'"
    with pytest.raises(AssertionError):
        binary_search_tree_0.get_next_node(node_0)


def test_case_9():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.iterate_postorder()
    var_1 = binary_search_tree_0.__getitem__(binary_search_tree_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    bool_0 = binary_search_tree_0.__delitem__(binary_search_tree_0)
    assert bool_0 is False
    none_type_0 = binary_search_tree_0.insert(bool_0)
    assert len(binary_search_tree_0) == 1
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 1
    var_0 = binary_search_tree_0.iterate_preorder()
    binary_search_tree_0.get_next_node(var_0)


def test_case_11():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.__repr__()
    assert var_0 == ""
    node_0 = module_0.Node(binary_search_tree_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert (
        f"{type(node_0.value).__module__}.{type(node_0.value).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(node_0.value) == 0
    generator_0 = binary_search_tree_0.iterate_nodes_by_depth(binary_search_tree_0)
    none_type_0 = binary_search_tree_0.insert(binary_search_tree_0)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    with pytest.raises(AssertionError):
        binary_search_tree_0.get_next_node(node_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    bool_0 = binary_search_tree_0.__contains__(binary_search_tree_0)
    assert bool_0 is False
    var_0 = binary_search_tree_0.__len__()
    assert var_0 == 0
    var_0.insert(var_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    bool_0 = False
    none_type_0 = binary_search_tree_0.insert(bool_0)
    assert len(binary_search_tree_0) == 1
    var_0 = binary_search_tree_0.__repr__()
    assert var_0 == "False"
    var_0.height()


@pytest.mark.xfail(strict=True)
def test_case_14():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.iterate_postorder()
    none_type_0 = None
    var_1 = binary_search_tree_0.__repr__()
    assert var_1 == ""
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 0
    node_0 = module_0.Node(none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert node_0.value is None
    generator_0 = binary_search_tree_0.iterate_nodes_by_depth(binary_search_tree_0)
    none_type_1 = binary_search_tree_0.insert(binary_search_tree_0)
    assert len(binary_search_tree_0) == 1
    binary_search_tree_0.get_next_node(node_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
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
    var_0 = binary_search_tree_0.iterate_leaves()
    var_1 = binary_search_tree_0.__len__()
    assert var_1 == 0
    node_0 = module_0.Node(binary_search_tree_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert (
        f"{type(node_0.value).__module__}.{type(node_0.value).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(node_0.value) == 0
    generator_0 = binary_search_tree_0.iterate_nodes_by_depth(binary_search_tree_0)
    none_type_0 = binary_search_tree_1.insert(binary_search_tree_1)
    assert len(binary_search_tree_1) == 1
    binary_search_tree_1.__getitem__(var_0)


@pytest.mark.xfail(strict=True)
def test_case_16():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.__repr__()
    assert var_0 == ""
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 0
    var_1 = binary_search_tree_0.__getitem__(var_0)
    var_2 = var_0.__len__()
    assert var_2 == 0
    none_type_0 = binary_search_tree_0.insert(var_0)
    assert len(binary_search_tree_0) == 1
    int_1 = binary_search_tree_0.height()
    assert int_1 == 1
    none_type_1 = binary_search_tree_0.insert(var_0)
    assert len(binary_search_tree_0) == 2
    var_2.depth()


@pytest.mark.xfail(strict=True)
def test_case_17():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    node_0 = module_0.Node(binary_search_tree_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert (
        f"{type(node_0.value).__module__}.{type(node_0.value).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(node_0.value) == 0
    none_type_0 = None
    bool_0 = True
    binary_search_tree_0.repr_traverse(none_type_0, none_type_0, node_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_18():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.iterate_postorder()
    var_1 = binary_search_tree_0.iterate_postorder()
    bool_0 = binary_search_tree_0.__contains__(var_0)
    assert bool_0 is False
    protocol_0 = module_1.Protocol(*var_1)
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
    var_1.repr_traverse(var_0, var_0, var_1, var_0)


@pytest.mark.xfail(strict=True)
def test_case_19():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    bool_0 = binary_search_tree_0.__delitem__(binary_search_tree_0)
    assert bool_0 is False
    none_type_0 = binary_search_tree_0.insert(bool_0)
    assert len(binary_search_tree_0) == 1
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 1
    binary_search_tree_0.__delitem__(list_0)


@pytest.mark.xfail(strict=True)
def test_case_20():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    bool_0 = binary_search_tree_0.__delitem__(binary_search_tree_0)
    assert bool_0 is False
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    none_type_0 = binary_search_tree_0.insert(bool_0)
    assert len(binary_search_tree_0) == 1
    var_0 = binary_search_tree_0.get_root()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "bst.Node"
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.value is False
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 1
    int_1 = 532
    bool_1 = binary_search_tree_0.__delitem__(int_1)
    assert bool_1 is False
    none_type_0.parent_path(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_21():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    none_type_0 = None
    bytes_0 = b"{\xddq\x99\xb4\xb5n\xb2\xbe~\xa9\xdaw&\x94\xfe?\xbe"
    bool_0 = binary_search_tree_0.__delitem__(bytes_0)
    assert bool_0 is False
    var_0 = binary_search_tree_0.__repr__()
    assert var_0 == ""
    list_0 = binary_search_tree_0.parent_path(var_0)
    none_type_1 = binary_search_tree_0.insert(var_0)
    assert len(binary_search_tree_0) == 1
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 1
    bool_1 = binary_search_tree_0.__delitem__(var_0)
    assert bool_1 is True
    assert len(binary_search_tree_0) == 0
    var_1 = none_type_0.__repr__()
    assert var_1 == "None"
    var_2 = binary_search_tree_0.iterate_preorder()
    var_1.iterate_leaves()


@pytest.mark.xfail(strict=True)
def test_case_22():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    bool_0 = binary_search_tree_0.__delitem__(binary_search_tree_0)
    assert bool_0 is False
    none_type_0 = binary_search_tree_0.insert(bool_0)
    assert len(binary_search_tree_0) == 1
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 1
    none_type_1 = binary_search_tree_0.insert(int_0)
    assert len(binary_search_tree_0) == 2
    int_1 = binary_search_tree_0.depth()
    assert int_1 == 2
    var_0 = binary_search_tree_0.iterate_postorder()
    var_0.__delitem__(var_0)


@pytest.mark.xfail(strict=True)
def test_case_23():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    bool_0 = binary_search_tree_0.__delitem__(binary_search_tree_0)
    assert bool_0 is False
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    none_type_0 = binary_search_tree_0.insert(bool_0)
    assert len(binary_search_tree_0) == 1
    var_0 = binary_search_tree_0.get_root()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "bst.Node"
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.value is False
    int_0 = 532
    bool_1 = binary_search_tree_0.__delitem__(int_0)
    assert bool_1 is False
    var_1 = binary_search_tree_0.get_next_node(var_0)
    var_2 = binary_search_tree_0.iterate_postorder()
    var_1.iterate_leaves()


@pytest.mark.xfail(strict=True)
def test_case_24():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    bytes_0 = b"{\xddq\x99\xb4\xb5n\xb2\xbe~\xa9\xdaw&\x94\xfe?\xbe"
    bool_0 = binary_search_tree_0.__delitem__(bytes_0)
    assert bool_0 is False
    var_0 = binary_search_tree_0.__repr__()
    assert var_0 == ""
    none_type_0 = binary_search_tree_0.insert(var_0)
    assert len(binary_search_tree_0) == 1
    bool_1 = binary_search_tree_0.__contains__(var_0)
    assert bool_1 is True
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 1
    var_1 = binary_search_tree_0.iterate_postorder()
    bool_2 = binary_search_tree_0.__delitem__(var_0)
    assert bool_2 is True
    assert len(binary_search_tree_0) == 0
    var_2 = var_1.__repr__()
    binary_search_tree_0.repr_traverse(var_2, var_1, var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_25():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.__repr__()
    assert var_0 == ""
    bool_0 = binary_search_tree_0.__delitem__(binary_search_tree_0)
    assert bool_0 is False
    bool_1 = var_0.__contains__(var_0)
    assert bool_1 is True
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    none_type_0 = binary_search_tree_0.insert(bool_0)
    assert len(binary_search_tree_0) == 1
    var_1 = binary_search_tree_0.get_root()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "bst.Node"
    assert var_1.left is None
    assert var_1.right is None
    assert var_1.value is False
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 1
    int_1 = -147
    bool_2 = binary_search_tree_0.__delitem__(int_1)
    assert bool_2 is False
    var_2 = binary_search_tree_0.get_root()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "bst.Node"
    assert var_2.left is None
    assert var_2.right is None
    assert var_2.value is False
    var_3 = binary_search_tree_0.get_next_node(var_1)
    var_4 = binary_search_tree_0.iterate_postorder()
    var_4.get_next_node(var_3)