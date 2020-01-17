from aj_code.PriorityQueue import PriorityQueue
from aj_code.Tree import LinkedBinaryTree
class LinkedBasedPriorityQueue(PriorityQueue):
    class _Node:
        __slots__ = 'value', 'parent', 'left', 'right'
        def __init__(self, e, parent=None, left=None, right=None):
            self.value = e
            self.parent = parent
            self.left = left
            self.right = right

    class Position:
        def __init__(self, node, container):
            self.node = node
            self.container = container

        def element(self):
            return self.node.value

        def __eq__(self, other):
            return type(self) is type(other) and self.node is other.node

    def __init__(self):
        self.data = LinkedBinaryTree()
        self.last = self.data.root()

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def min(self):
        return self.root

    def add(self, k, v):
        if self.size == 0:
            self.root = self._Node(k, v, None, None, None)
            self.size += 1
        else:
            self.traverse(self.root)

    def traverse(self, node):
        if node.left is not None:
            self.traverse(node.left)

        elif node.right is not None:
            self.traverse(node.right)

tree = LinkedBasedPriorityQueue()
tree.add(1, 2)
tree.add(9, 4)
tree.add(8, 3)
tree.add(4, 2)
tree.add(2, 10)
print((tree.min).key)
print(tree.is_empty())
print(len(tree))