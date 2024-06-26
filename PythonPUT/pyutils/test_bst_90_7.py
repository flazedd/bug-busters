# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bst as module_0
import builtins as module_1
import typing as module_2


def test_case_0():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0


def test_case_1():
    none_type_0 = None
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.__getitem__(none_type_0)


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
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 0
    var_0 = binary_search_tree_0.iterate_preorder()
    var_0.iterate_leaves()


@pytest.mark.xfail(strict=True)
def test_case_4():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    binary_search_tree_0.repr_traverse(
        binary_search_tree_0,
        binary_search_tree_0,
        binary_search_tree_0,
        binary_search_tree_0,
    )


def test_case_5():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.__repr__()
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_6():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 0
    var_0 = binary_search_tree_0.iterate_preorder()
    var_1 = binary_search_tree_0.get_root()
    var_0.iterate_leaves()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "r|5p{%60%1&\n(C0}p"
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    bool_0 = binary_search_tree_0.__delitem__(str_0)
    assert bool_0 is False
    binary_search_tree_1 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_1).__module__}.{type(binary_search_tree_1).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_1) == 0
    var_0 = binary_search_tree_0.__len__()
    assert var_0 == 0
    var_1 = binary_search_tree_0.__getitem__(var_0)
    var_1.iterate_postorder()


def test_case_8():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    bool_0 = True
    var_0 = binary_search_tree_0.__getitem__(bool_0)
    bool_1 = binary_search_tree_0.__contains__(bool_0)
    assert bool_1 is False
    var_1 = binary_search_tree_0.__repr__()
    assert var_1 == ""


def test_case_9():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 0
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    bytes_0 = b""
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    int_1 = binary_search_tree_0.height()
    assert int_1 == 1
    var_0 = binary_search_tree_0.iterate_postorder()


@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "r|5p{%60%1&\n(C0}p"
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    bool_0 = binary_search_tree_0.__delitem__(str_0)
    assert bool_0 is False
    binary_search_tree_1 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_1).__module__}.{type(binary_search_tree_1).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_1) == 0
    var_0 = binary_search_tree_1.iterate_leaves()
    var_0.__len__()


@pytest.mark.xfail(strict=True)
def test_case_11():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.__getitem__(binary_search_tree_0)
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
    none_type_1 = binary_search_tree_0.insert(none_type_0)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    var_1 = binary_search_tree_0.__repr__()
    assert var_1 == "None"
    var_1.get_next_node(node_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    bytes_0 = b""
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    bool_0 = binary_search_tree_0.__delitem__(bytes_0)
    assert bool_0 is True
    assert len(binary_search_tree_0) == 0
    binary_search_tree_0.get_next_node(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
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
    none_type_1 = binary_search_tree_0.insert(none_type_0)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 1
    binary_search_tree_0.get_next_node(node_0)


def test_case_14():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    bytes_0 = b""
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    int_0 = binary_search_tree_0.height()
    assert int_0 == 1
    none_type_1 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 2
    bool_0 = binary_search_tree_0.__delitem__(bytes_0)
    assert bool_0 is True
    assert len(binary_search_tree_0) == 1
    var_0 = binary_search_tree_0.__repr__()
    assert var_0 == "b''\n└──b''"


@pytest.mark.xfail(strict=True)
def test_case_15():
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
    str_0 = 'p9rO"P%t'
    str_1 = binary_search_tree_0.repr_traverse(str_0, str_0, node_0, str_0)
    assert str_1 == '\np9rO"P%tp9rO"P%t'
    none_type_0 = None
    list_0 = binary_search_tree_0.parent_path(str_0)
    none_type_1 = binary_search_tree_0.insert(list_0)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    list_1 = [none_type_0, none_type_1]
    bool_0 = binary_search_tree_0.__delitem__(list_1)
    assert bool_0 is False
    var_0 = binary_search_tree_0.__getitem__(list_1)
    binary_search_tree_0.get_next_node(node_0)


def test_case_16():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    bytes_0 = b""
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    int_0 = binary_search_tree_0.height()
    assert int_0 == 1
    none_type_1 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 2
    var_0 = binary_search_tree_0.iterate_postorder()
    var_1 = binary_search_tree_0.__getitem__(bytes_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "bst.Node"
    assert var_1.left is None
    assert (
        f"{type(var_1.right).__module__}.{type(var_1.right).__qualname__}" == "bst.Node"
    )
    assert var_1.value == b""
    var_2 = binary_search_tree_0.iterate_inorder()
    var_3 = binary_search_tree_0.get_next_node(var_1)
    assert f"{type(var_3).__module__}.{type(var_3).__qualname__}" == "bst.Node"
    assert var_3.left is None
    assert var_3.right is None
    assert var_3.value == b""


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
    list_0 = binary_search_tree_0.parent_path(node_0)
    str_0 = 'p9rO"P%t'
    none_type_0 = None
    list_1 = binary_search_tree_0.parent_path(str_0)
    none_type_1 = binary_search_tree_0.insert(list_1)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    list_2 = [none_type_0, none_type_0]
    bool_0 = binary_search_tree_0.__delitem__(list_2)
    assert bool_0 is False
    var_0 = binary_search_tree_0.__getitem__(list_2)
    binary_search_tree_0.get_next_node(node_0)


def test_case_18():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.iterate_nodes_by_depth(binary_search_tree_0)
    str_0 = 'p9rO"P%t'
    none_type_0 = None
    list_0 = binary_search_tree_0.parent_path(str_0)
    none_type_1 = binary_search_tree_0.insert(list_0)
    assert len(binary_search_tree_0) == 1
    list_1 = [none_type_0, var_0]
    bool_0 = binary_search_tree_0.__delitem__(list_1)
    assert bool_0 is False


def test_case_19():
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
    set_0 = {binary_search_tree_0, node_0, node_0}
    var_0 = binary_search_tree_0.__getitem__(set_0)
    str_0 = 'p9rO"P%t'
    none_type_0 = None
    list_0 = binary_search_tree_0.parent_path(str_0)
    none_type_1 = binary_search_tree_0.insert(list_0)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    list_1 = [none_type_0, var_0]
    var_1 = binary_search_tree_0.__getitem__(list_1)
    var_2 = binary_search_tree_0.get_root()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "bst.Node"
    assert var_2.left is None
    assert var_2.right is None
    assert var_2.value == [None]
    var_3 = binary_search_tree_0.get_next_node(var_2)


def test_case_20():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 0
    none_type_0 = None
    none_type_1 = binary_search_tree_0.insert(none_type_0)
    assert len(binary_search_tree_0) == 1
    node_0 = module_0.Node(none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert node_0.value is None
    int_1 = binary_search_tree_0.depth()
    assert int_1 == 1
    with pytest.raises(AssertionError):
        binary_search_tree_0.get_next_node(node_0)


def test_case_21():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    bytes_0 = b""
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    none_type_1 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 2


def test_case_22():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.iterate_preorder()
    node_0 = module_0.Node(binary_search_tree_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert (
        f"{type(node_0.value).__module__}.{type(node_0.value).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(node_0.value) == 0
    set_0 = {node_0, node_0}
    var_1 = binary_search_tree_0.__getitem__(set_0)
    var_2 = binary_search_tree_0.iterate_postorder()
    list_0 = binary_search_tree_0.parent_path(set_0)
    none_type_0 = binary_search_tree_0.insert(list_0)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    list_1 = []
    bool_0 = binary_search_tree_0.__delitem__(list_1)
    assert bool_0 is False
    var_3 = binary_search_tree_0.__getitem__(list_1)
    node_1 = module_0.Node(binary_search_tree_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "bst.Node"
    assert node_1.left is None
    assert node_1.right is None
    assert (
        f"{type(node_1.value).__module__}.{type(node_1.value).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(node_1.value) == 1


def test_case_23():
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
    var_0 = binary_search_tree_0.iterate_preorder()
    none_type_0 = var_0.__repr__()
    var_1 = binary_search_tree_0.iterate_preorder()
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 0
    var_2 = binary_search_tree_0.iterate_preorder()
    var_3 = binary_search_tree_0.iterate_preorder()
    object_0 = module_1.object(*var_2)
    generic_0 = module_2.Generic(*var_0)
    assert (
        f"{type(generic_0).__module__}.{type(generic_0).__qualname__}"
        == "typing.Generic"
    )
    assert module_2.EXCLUDED_ATTRIBUTES == [
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
        f"{type(module_2.T).__module__}.{type(module_2.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.KT).__module__}.{type(module_2.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.VT).__module__}.{type(module_2.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.T_co).__module__}.{type(module_2.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.V_co).__module__}.{type(module_2.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.VT_co).__module__}.{type(module_2.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.T_contra).__module__}.{type(module_2.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.CT_co).__module__}.{type(module_2.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.AnyStr).__module__}.{type(module_2.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_2.TYPE_CHECKING is False
    with pytest.raises(AssertionError):
        binary_search_tree_0.get_next_node(node_0)


def test_case_24():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    bytes_0 = b""
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    none_type_1 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 2
    bool_0 = binary_search_tree_0.__delitem__(bytes_0)
    assert bool_0 is True
    assert len(binary_search_tree_0) == 1


def test_case_25():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    bytes_0 = b""
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    int_0 = binary_search_tree_0.iterate_preorder()
    none_type_1 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 2
    bool_0 = binary_search_tree_0.__delitem__(bytes_0)
    assert bool_0 is True
    assert len(binary_search_tree_0) == 1
    int_1 = binary_search_tree_0.depth()
    assert int_1 == 2
    var_0 = binary_search_tree_0.__repr__()
    assert var_0 == "b''\n└──b''"


@pytest.mark.xfail(strict=True)
def test_case_26():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    var_0 = binary_search_tree_0.iterate_preorder()
    none_type_0 = binary_search_tree_0.insert(var_0)
    assert len(binary_search_tree_0) == 1
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 1
    var_1 = binary_search_tree_0.iterate_preorder()
    module_2.Generic(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_27():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
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
    list_0 = binary_search_tree_0.parent_path(binary_search_tree_0)
    bytes_0 = b""
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    var_0 = binary_search_tree_0.__len__()
    assert var_0 == 1
    none_type_1 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 2
    assert len(node_0.value) == 2
    bool_0 = binary_search_tree_0.__delitem__(bytes_0)
    assert bool_0 is True
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    str_0 = "E?9^hN5V*|mtj3Ah=Ag"
    float_0 = 1835.32
    str_1 = binary_search_tree_0.repr_traverse(
        str_0, float_0, node_0, binary_search_tree_0
    )
    assert str_1 == "\nE?9^hN5V*|mtj3Ah=Ag1835.32b''\n└──b''"
    str_2 = "-K`f!s.^H<NsCwf1:"
    int_1 = binary_search_tree_0.depth()
    assert int_1 == 2
    generator_0 = binary_search_tree_0.get_nodes_in_range_inclusive(str_2, bool_0)
    none_type_2 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 2
    assert len(node_0.value) == 2
    binary_search_tree_1 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_1).__module__}.{type(binary_search_tree_1).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_1) == 0
    var_1 = binary_search_tree_1.iterate_postorder()
    var_1.get_nodes_in_range_inclusive(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_28():
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
    bytes_0 = b""
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    none_type_1 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 2
    assert len(node_0.value) == 2
    bool_0 = binary_search_tree_0.__delitem__(bytes_0)
    assert bool_0 is True
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    int_0 = binary_search_tree_0.height()
    assert int_0 == 2
    set_0 = {node_0, none_type_0}
    node_1 = module_0.Node(set_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "bst.Node"
    assert node_1.left is None
    assert node_1.right is None
    assert (
        f"{type(node_1.value).__module__}.{type(node_1.value).__qualname__}"
        == "builtins.set"
    )
    assert len(node_1.value) == 2
    bytes_1 = b"\x16\x1a\xbda-\xe3&\xbf\xd6k\xa0\xf9]"
    var_0 = binary_search_tree_0.__getitem__(bytes_1)
    var_1 = binary_search_tree_0.iterate_inorder()
    binary_search_tree_0.get_next_node(node_0)


@pytest.mark.xfail(strict=True)
def test_case_29():
    binary_search_tree_0 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_0).__module__}.{type(binary_search_tree_0).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_0) == 0
    int_0 = binary_search_tree_0.depth()
    assert int_0 == 0
    bytes_0 = b""
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    var_0 = binary_search_tree_0.get_root()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "bst.Node"
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.value == b""
    none_type_1 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 2
    assert (
        f"{type(var_0.right).__module__}.{type(var_0.right).__qualname__}" == "bst.Node"
    )
    bool_0 = binary_search_tree_0.__delitem__(bytes_0)
    assert bool_0 is True
    assert len(binary_search_tree_0) == 1
    str_0 = "E?9^hN5V*|mtj3Ah=Ag"
    float_0 = 1835.9208569586874
    str_1 = binary_search_tree_0.repr_traverse(
        str_0, float_0, var_0, binary_search_tree_0
    )
    assert (
        str_1
        == "\nE?9^hN5V*|mtj3Ah=Ag1835.9208569586874b''\nE?9^hN5V*|mtj3Ah=Ag│  └──b''"
    )
    set_0 = {bytes_0, var_0, none_type_0}
    node_0 = module_0.Node(set_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "bst.Node"
    assert node_0.left is None
    assert node_0.right is None
    assert (
        f"{type(node_0.value).__module__}.{type(node_0.value).__qualname__}"
        == "builtins.set"
    )
    assert len(node_0.value) == 3
    var_1 = binary_search_tree_0.__getitem__(bytes_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "bst.Node"
    assert var_1.left is None
    assert (
        f"{type(var_1.right).__module__}.{type(var_1.right).__qualname__}" == "bst.Node"
    )
    assert var_1.value == b""
    binary_search_tree_0.__getitem__(str_1)


@pytest.mark.xfail(strict=True)
def test_case_30():
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
    int_0 = binary_search_tree_0.height()
    assert int_0 == 0
    int_1 = binary_search_tree_0.depth()
    assert int_1 == 0
    generator_0 = binary_search_tree_0.iterate_nodes_by_depth(binary_search_tree_0)
    var_0 = binary_search_tree_0.iterate_leaves()
    bytes_0 = b"\xca\xebf\xd7\x84\xfc\xa7\x97\xc2\x92"
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    var_1 = binary_search_tree_0.get_root()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "bst.Node"
    assert var_1.left is None
    assert var_1.right is None
    assert var_1.value == b"\xca\xebf\xd7\x84\xfc\xa7\x97\xc2\x92"
    int_2 = binary_search_tree_0.height()
    assert int_2 == 1
    bool_0 = binary_search_tree_0.__delitem__(bytes_0)
    assert bool_0 is True
    assert len(binary_search_tree_0) == 0
    assert len(node_0.value) == 0
    str_0 = "k&7D{|!\x0bW3F"
    str_1 = binary_search_tree_0.repr_traverse(str_0, int_2, var_1, bool_0)
    assert str_1 == "\nk&7D{|!\x0bW3F1b'\\xca\\xebf\\xd7\\x84\\xfc\\xa7\\x97\\xc2\\x92'"
    str_2 = "ANNoccNJT|l6"
    float_0 = 1835.9208569586874
    str_3 = binary_search_tree_0.repr_traverse(
        str_2, float_0, node_0, binary_search_tree_0
    )
    assert str_3 == "\nANNoccNJT|l61835.9208569586874"
    node_1 = module_0.Node(var_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "bst.Node"
    assert node_1.left is None
    assert node_1.right is None
    assert (
        f"{type(node_1.value).__module__}.{type(node_1.value).__qualname__}"
        == "builtins.generator"
    )
    binary_search_tree_1 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_1).__module__}.{type(binary_search_tree_1).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_1) == 0
    generic_0 = module_2.Generic(*var_0)
    assert (
        f"{type(generic_0).__module__}.{type(generic_0).__qualname__}"
        == "typing.Generic"
    )
    assert module_2.EXCLUDED_ATTRIBUTES == [
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
        f"{type(module_2.T).__module__}.{type(module_2.T).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.KT).__module__}.{type(module_2.KT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.VT).__module__}.{type(module_2.VT).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.T_co).__module__}.{type(module_2.T_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.V_co).__module__}.{type(module_2.V_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.VT_co).__module__}.{type(module_2.VT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.T_contra).__module__}.{type(module_2.T_contra).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.CT_co).__module__}.{type(module_2.CT_co).__qualname__}"
        == "typing.TypeVar"
    )
    assert (
        f"{type(module_2.AnyStr).__module__}.{type(module_2.AnyStr).__qualname__}"
        == "typing.TypeVar"
    )
    assert module_2.TYPE_CHECKING is False
    binary_search_tree_2 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_2).__module__}.{type(binary_search_tree_2).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_2) == 0
    int_2.iterate_inorder()


@pytest.mark.xfail(strict=True)
def test_case_31():
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
    int_0 = binary_search_tree_0.height()
    assert int_0 == 0
    int_1 = binary_search_tree_0.depth()
    assert int_1 == 0
    generator_0 = binary_search_tree_0.iterate_nodes_by_depth(binary_search_tree_0)
    var_0 = binary_search_tree_0.iterate_leaves()
    bytes_0 = b"\xca\xebf\xd7\x84\xfc\xa7\x97\xc2\x92"
    none_type_0 = binary_search_tree_0.insert(bytes_0)
    assert len(binary_search_tree_0) == 1
    assert len(node_0.value) == 1
    var_1 = binary_search_tree_0.get_root()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "bst.Node"
    assert var_1.left is None
    assert var_1.right is None
    assert var_1.value == b"\xca\xebf\xd7\x84\xfc\xa7\x97\xc2\x92"
    int_2 = binary_search_tree_0.height()
    assert int_2 == 1
    str_0 = "ANNoccNJT|l6"
    float_0 = 1835.9208569586874
    str_1 = binary_search_tree_0.repr_traverse(
        str_0, float_0, node_0, binary_search_tree_0
    )
    assert (
        str_1
        == "\nANNoccNJT|l61835.9208569586874b'\\xca\\xebf\\xd7\\x84\\xfc\\xa7\\x97\\xc2\\x92'"
    )
    node_1 = module_0.Node(var_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "bst.Node"
    assert node_1.left is None
    assert node_1.right is None
    assert (
        f"{type(node_1.value).__module__}.{type(node_1.value).__qualname__}"
        == "builtins.generator"
    )
    binary_search_tree_1 = module_0.BinarySearchTree()
    assert (
        f"{type(binary_search_tree_1).__module__}.{type(binary_search_tree_1).__qualname__}"
        == "bst.BinarySearchTree"
    )
    assert len(binary_search_tree_1) == 0
    module_2.Generic(*var_0)
