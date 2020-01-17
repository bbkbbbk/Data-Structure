class LinkedBasedTree:
    class Node:
        __slots__ = 'value', 'parent', 'left', 'right'
        def __init__(self, v, p=None, l=None, r=None):
            self.value = v
            self.parent = p
            self.left = l
            self.right = r

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def add_root(self, n):
        new_node = self.Node(n)
        self.root = new_node
        return new_node


    def add_left(self, p, v):
        new_node = self.Node(v)
        new_node.parent = p
        p.left = new_node
        return new_node

    def add_right(self, p, v):
        new_node = self.Node(v)
        new_node.parent = p
        p.right = new_node
        return new_node

    def num_children(self, p):
        num = 0
        if p.left is not None:
            num += 1
        elif p.right is not None:
            num += 1
        return num

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_root(self, p):
        return self.root == p

    def children(self, p):
        if p.left is not None:
            yield p.left
        if p.right is not None:
            yield p.right

    def height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1+max(self.height(p) for p in self.children(p))

    def depth(self, node):
        if node == self.root:
            return 0
        return 1 + self.depth(node.parent)

    def pre_order_traversal(self, node, res):
        if node:
            res += (str(node.value) + ' ')
            res = self.pre_order_traversal(node.left, res)
            res = self.pre_order_traversal(node.right, res)
        return res

    def in_order_traversal(self, node, res):
        if node:
            res = self.in_order_traversal(node.left, res)
            res += (str(node.value) + ' ')
            res = self.in_order_traversal(node.right, res)
        return res

    def post_order_traversal(self, node, res):
        if node:
            res = self.post_order_traversal(node.left, res)
            res = self.post_order_traversal(node.right, res)
            res += (str(node.value) + ' ')
        return res

    def breadth_first(self, node, res):
        pass

    def find_sum(self, node, res):
        if node:
            res = self.find_sum(node.left, res)
            res = self.find_sum(node.right, res)
            depth = self.depth(node)
            res[depth] += node.value
        return res

tree = LinkedBasedTree()
p2 = tree.add_root(2)

p5 = tree.add_left(p2, 5)
p7 = tree.add_right(p2, 7)

p4 = tree.add_left(p5, -4)
p1 = tree.add_right(p5, 1)

p8 = tree.add_left(p1, 8)
p44 = tree.add_right(p1, 4)

p77 = tree.add_left(p44, 7)
p22 = tree.add_right(p44, 2)

p0 = tree.add_right(p7, 0)
p222 = tree.add_left(p0, -2)
p6 = tree.add_right(p0, 6)

p3 = tree.add_left(p6, 3)


print(tree.pre_order_traversal(tree.root, ''))
print(tree.in_order_traversal(tree.root, ''))
print(tree.post_order_traversal(tree.root, ''))
print(tree.depth(p6))
print(tree.height(p1))
sum_tree = tree.find_sum(tree.root, [0] * (tree.height(tree.root)+1))
print(sum_tree, sum(sum_tree))



