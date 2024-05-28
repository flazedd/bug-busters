from typing import Generator, List, Optional
from __type_hints import Comparable

class Node:
    def __init__(self, value: Comparable) -> None:
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.value: Comparable = value


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.count = 0
        self.traverse = None

    def get_root(self) -> Optional[Node]:
        return self.root

    def _on_insert(self, parent: Optional[Node], new: Node) -> None:
        pass

    def insert(self, value: Comparable) -> None:
        if self.root is None:
            self.root = Node(value)
            self.count = 1
            self._on_insert(None, self.root)
        else:
            self._insert(value, self.root)

    def _insert(self, value: Comparable, node: Node):
        """Insertion helper"""
        if value < node.value:
            if node.left is not None:
                self._insert(value, node.left)
            else:
                node.left = Node(value)
                self.count += 1
                self._on_insert(node, node.left)
        else:
            if node.right is not None:
                self._insert(value, node.right)
            else:
                node.right = Node(value)
                self.count += 1
                self._on_insert(node, node.right)

    def __getitem__(self, value: Comparable) -> Optional[Node]:
        if self.root is not None:
            return self._find_exact(value, self.root)
        return None

    def _find_exact(self, target: Comparable, node: Node) -> Optional[Node]:
        if target == node.value:
            return node
        elif target < node.value and node.left is not None:
            return self._find_exact(target, node.left)
        elif target > node.value and node.right is not None:
            return self._find_exact(target, node.right)
        return None

    def _find_lowest_node_less_than_or_equal_to(
        self, target: Comparable, node: Optional[Node]
    ) -> Optional[Node]:

        if not node:
            return None

        if target == node.value:
            return node

        elif target > node.value:
            if below := self._find_lowest_node_less_than_or_equal_to(
                target, node.right
            ):
                return below
            else:
                return node

        else:
            return self._find_lowest_node_less_than_or_equal_to(target, node.left)

    def _find_lowest_node_greater_than_or_equal_to(
        self, target: Comparable, node: Optional[Node]
    ) -> Optional[Node]:
        if not node:
            return None

        if target == node.value:
            return node

        elif target > node.value:
            return self._find_lowest_node_greater_than_or_equal_to(target, node.right)

        # If target < this node's value, either this node is the
        # answer or the answer is in this node's left subtree.
        else:
            if below := self._find_lowest_node_greater_than_or_equal_to(
                target, node.left
            ):
                return below
            else:
                return node

    def _parent_path(
        self, current: Optional[Node], target: Node
    ) -> List[Optional[Node]]:
        """Internal helper"""
        if current is None:
            return [None]
        ret: List[Optional[Node]] = [current]
        if target.value == current.value:
            return ret
        elif target.value < current.value:
            ret.extend(self._parent_path(current.left, target))
            return ret
        else:
            assert target.value > current.value
            ret.extend(self._parent_path(current.right, target))
            return ret

    def parent_path(self, node: Node) -> List[Optional[Node]]:
        return self._parent_path(self.root, node)

    def __delitem__(self, value: Comparable) -> bool:
        if self.root is not None:
            ret = self._delete(value, None, self.root)
            if ret:
                self.count -= 1
                if self.count == 0:
                    self.root = None
            return ret
        return False

    def _on_delete(self, parent: Optional[Node], deleted: Node) -> None:
        """This is called just after deleted was deleted from the tree"""
        pass

    def _delete(self, value: Comparable, parent: Optional[Node], node: Node) -> bool:
        """Delete helper"""
        if node.value == value:

            # Deleting a leaf node
            if node.left is None and node.right is None:
                if parent is not None:
                    if parent.left == node:
                        parent.left = None
                    else:
                        assert parent.right == node
                        parent.right = None
                self._on_delete(parent, node)
                return True

            # Node only has a right.
            elif node.left is None:
                assert node.right is not None
                if parent is not None:
                    if parent.left == node:
                        parent.left = node.right
                    else:
                        assert parent.right == node
                        parent.right = node.right
                self._on_delete(parent, node)
                return True

            # Node only has a left.
            elif node.right is None:
                assert node.left is not None
                if parent is not None:
                    if parent.left == node:
                        parent.left = node.left
                    else:
                        assert parent.right == node
                        parent.right = node.left
                self._on_delete(parent, node)
                return True

            else:
                assert node.left is not None and node.right is not None
                successor = self.get_next_node(node)
                assert successor is not None
                node.value = successor.value
                return self._delete(node.value, node, node.right)

        elif value < node.value and node.left is not None:
            return self._delete(value, node, node.left)
        elif value > node.value and node.right is not None:
            return self._delete(value, node, node.right)
        return False

    def __len__(self):
        return self.count

    def __contains__(self, value: Comparable) -> bool:
        return self.__getitem__(value) is not None

    def _iterate_preorder(self, node: Node):
        yield node.value
        if node.left is not None:
            yield from self._iterate_preorder(node.left)
        if node.right is not None:
            yield from self._iterate_preorder(node.right)

    def _iterate_inorder(self, node: Node):
        if node.left is not None:
            yield from self._iterate_inorder(node.left)
        yield node.value
        if node.right is not None:
            yield from self._iterate_inorder(node.right)

    def _iterate_postorder(self, node: Node):
        if node.left is not None:
            yield from self._iterate_postorder(node.left)
        if node.right is not None:
            yield from self._iterate_postorder(node.right)
        yield node.value

    def iterate_preorder(self):
        if self.root is not None:
            yield from self._iterate_preorder(self.root)

    def iterate_inorder(self):
        if self.root is not None:
            yield from self._iterate_inorder(self.root)

    def iterate_postorder(self):
        if self.root is not None:
            yield from self._iterate_postorder(self.root)

    def _iterate_leaves(self, node: Node):
        if node.left is not None:
            yield from self._iterate_leaves(node.left)
        if node.right is not None:
            yield from self._iterate_leaves(node.right)
        if node.left is None and node.right is None:
            yield node.value

    def iterate_leaves(self):
        if self.root is not None:
            yield from self._iterate_leaves(self.root)

    def _iterate_by_depth(self, node: Node, depth: int):
        if depth == 0:
            yield node.value
        else:
            assert depth > 0
            if node.left is not None:
                yield from self._iterate_by_depth(node.left, depth - 1)
            if node.right is not None:
                yield from self._iterate_by_depth(node.right, depth - 1)

    def iterate_nodes_by_depth(self, depth: int) -> Generator[Node, None, None]:
        if self.root is not None:
            yield from self._iterate_by_depth(self.root, depth)

    def get_next_node(self, node: Node) -> Optional[Node]:
        if node.right is not None:
            x = node.right
            while x.left is not None:
                x = x.left
            return x

        path = self.parent_path(node)
        assert path[-1] is not None
        assert path[-1] == node
        path = path[:-1]
        path.reverse()
        for ancestor in path:
            assert ancestor is not None
            if node != ancestor.right:
                return ancestor
            node = ancestor
        return None

    def get_nodes_in_range_inclusive(
        self, lower: Comparable, upper: Comparable
    ) -> Generator[Node, None, None]:
        node: Optional[Node] = self._find_lowest_node_greater_than_or_equal_to(
            lower, self.root
        )
        while node:
            if lower <= node.value <= upper:
                yield node
            node = self.get_next_node(node)

    def _depth(self, node: Node, sofar: int) -> int:
        depth_left = sofar + 1
        depth_right = sofar + 1
        if node.left is not None:
            depth_left = self._depth(node.left, sofar + 1)
        if node.right is not None:
            depth_right = self._depth(node.right, sofar + 1)
        return max(depth_left, depth_right)

    def depth(self) -> int:
        if self.root is None:
            return 0
        return self._depth(self.root, 0)

    def height(self) -> int:
        """Returns the height (i.e. max depth) of the tree"""
        return self.depth()

    def repr_traverse(
        self,
        padding: str,
        pointer: str,
        node: Optional[Node],
        has_right_sibling: bool,
    ) -> str:
        if node is not None:
            viz = f"\n{padding}{pointer}{node.value}"
            if has_right_sibling:
                padding += "│  "
            else:
                padding += "   "

            pointer_right = "└──"
            if node.right is not None:
                pointer_left = "├──"
            else:
                pointer_left = "└──"

            viz += self.repr_traverse(
                padding, pointer_left, node.left, node.right is not None
            )
            viz += self.repr_traverse(padding, pointer_right, node.right, False)
            return viz
        return ""

    def __repr__(self):
        if self.root is None:
            return ""

        ret = f"{self.root.value}"
        pointer_right = "└──"
        if self.root.right is None:
            pointer_left = "└──"
        else:
            pointer_left = "├──"

        ret += self.repr_traverse(
            "", pointer_left, self.root.left, self.root.left is not None
        )
        ret += self.repr_traverse("", pointer_right, self.root.right, False)
        return ret


if __name__ == "__main__":
    import doctest

    doctest.testmod()