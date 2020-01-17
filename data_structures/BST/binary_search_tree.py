class BinarySearchTree:
    class Node:
        def __init__(self, k, p=None):
            self.key = k
            self.parent = p
            self.left = self.right = None

    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def _add_root(self, k):
        self.root = self.Node(k)

    def _add_left(self, p, node):
        if p.left is None:
            p.left = node
        else:
            raise KeyError('Left node already exists')

    def _add_right(self, p, node):
        if p.right is None:
            p.right = node
        else:
            raise KeyError('Right node already exists')

    def find_min(self, root):
        node = root

        while node.left is not None:
            node = node.left
        return node

    def find_max(self, root):
        node = root

        while node.right is not None:
            node = node.right
        return node

    def num_children(self, p):
        count = 0

        if p.left is not None:
            count += 1
        elif p.right is not None:
            count += 1
        return count

    def is_left_child(self, node):
        return node.parent and node.parent.left == self

    def is_right_child(self, node):
        return node.parent and node.parent.right == self

    def search(self, k):
        if self.is_empty():
            print('Tree is empty')

        node = self._search(self.root, k)

        if node.key == k:
            print('Search for key: {}: Found'.format(k))
        else:
            print('Search for key: {}: Not found'.format(k))

    def _search(self, node, k):
        if node.key == k:
            return node

        if k < node.key:
            if node.left is not None:
                # since left tre contains lesser value
                return self._search(node.left, k)
        else:
            if node.right is not None:
                # since right tree contains greater value
                return self._search(node.right, k)
        # if not find the exact same key will return the position to be inserted
        return node

    def insert(self, k):
        if self.is_empty():
            self._add_root(k)
            self.size += 1
            return

        parent = self._search(self.root, k)
        new_node = self.Node(k, parent)

        if k < parent.key:
            self._add_left(parent, new_node)
        else:
            self._add_right(parent, new_node)

        self.size += 1

    def delete(self, key):
        if self._delete(self.root, key):
            print('Delete key {}: succeed'.format(key))
            self.size -= 1
        else:
            print('Delete key {}: failed'.format(key))

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.find_max(root.left)  # or temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)
        return root

    def in_order_traversal(self):
        print('In-order Traversal:', self._in_order_traversal(self.root, []))

    def _in_order_traversal(self, node, res=[]):
        if node:
            res = self._in_order_traversal(node.left, res)
            res += [node.key]
            res = self._in_order_traversal(node.right, res)
        return res

    def pre_order_traversal(self):
        print('Pre-order traversal:', self._pre_order_traversal(self.root, []))

    def _pre_order_traversal(self, node, res=[]):
        if node:
            res += [node.key]
            res = self._pre_order_traversal(node.left, res)
            res = self._pre_order_traversal(node.right, res)
        return res


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(6)
    tree.insert(2)
    tree.insert(4)
    tree.insert(8)
    tree.pre_order_traversal()

    tree.search(2)
    tree.search(1)

    tree.delete(6)
    tree.pre_order_traversal()