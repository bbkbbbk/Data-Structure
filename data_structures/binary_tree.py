class Tree:
    class Node:
        __slots__ = 'value', 'parent', 'left', 'right'

        def __init__(self, v, p=None, l=None, r=None):
            self.value = v
            self.parent = p
            self.left = l
            self.right = r

        def __eq__(self, other):
            return self.value == other.value

        def __gt__(self, other):
            return self.value > other.value

        def __ge__(self, other):
            return self.value >= other.value

        def __lt__(self, other):
            return self.value < other.value

        def __le__(self, other):
            return self.value <= other.value

    def __init__(self):
        self.root = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size

    def add_root(self, v):
        if self.root is None:
            node = self.Node(v)
            self.root = node
            self.size += 1
            return node
        else:
            raise KeyError('Root already exists')

    def add_node(self, p, v):
        if p.left is None:
            new_node = self.Node(v)
            p.left = new_node
            new_node.parent = p
            self.size += 1
            self.last = new_node
            return new_node
        elif p.left is not None and p.right is None:
            new_node = self.Node(v)
            if p.left.value < v:
                p.right = new_node
                new_node.parent = p
                self.size += 1
                self.last = new_node
                return new_node
            else:
                p.right = p.left
                p.left = new_node
                new_node.parent = p
                self.last = new_node
                self.size += 1
                return new_node
        # elif p.left is not None and p.right is not None:
        #     raise KeyError('Both left and right already exist')

    def insert(self, v, root):
        if v < root.value:
            if root.left is None:
                root.left = self.Node(v)
                return root.left
            else:
                self.insert(v, root.left)
        else:
            if root.right is None:
                root.right = self.Node(v)
                return root.right
            else:
                self.insert(v, root.right)

    def add_left(self, p, v):
        if p.left is None:
            new_node = self.Node(v)
            p.left = new_node
            new_node.parent = p
            return new_node
        else:
            raise KeyError('Left node already exists')

    def add_right(self, p, v):
        if p.right is None:
            new_node = self.Node(v)
            p.right = new_node
            new_node.parent = p
            return new_node
        else:
            raise KeyError('Right node already exists')

    def num_children(self, p):
        num = 0
        if p.left is not None:
            num += 1
        elif p.right is not None:
            num += 1
        return num

    def children(self, p):
        if p.left is not None:
            yield p.left
        if p.right is not None:
            yield p.right

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_root(self, p):
        return self.root == p

    def height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(p) for p in self.children(p))

    def depth(self, node):
        if node == self.root:
            return 0
        return 1 + self.depth(node.parent)

    def binary_search_tree(self, root, key):
        if root is None:
            return None

        if root is not None and root.value == key:
            return root

        if root.value < key:
            return self.binary_search_tree(root.right, key)

        return self.binary_search_tree(root.left, key)

    def pre_order_traversal(self, node, res=[]):
        if node:
            res += [node.value]
            res = self.pre_order_traversal(node.left, res)
            res = self.pre_order_traversal(node.right, res)
        return res

    def in_order_traversal(self, node, res=[]):
        if node:
            res = self.pre_order_traversal(node.left, res)
            res += [node.value]
            res = self.pre_order_traversal(node.right, res)
        return res

    def __iter__(self):
        nodes = self.pre_order_traversal(self.root, [])
        for node in nodes:
            yield node


if __name__ == '__main__':
    t = Tree()
    root = t.add_root(8)
    node_3 = t.insert(3, t.root)
    node_10 = t.insert(10, t.root)

    node_1 = t.insert(1, t.root)
    node_6 = t.insert(6, t.root)

    node_14 = t.insert(14, t.root)

    node_4 = t.insert(4, t.root)
    node_7 = t.insert(7, t.root)
    print(t.pre_order_traversal(t.root))
