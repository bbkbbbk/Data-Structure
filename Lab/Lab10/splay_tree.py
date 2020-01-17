class SplayTree:
    class Node:
        __slots__ = 'key', 'left', 'right'

        def __init__(self, key):
            self.key = key
            self.left = self.right = None

    __slots__ = 'root'

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = self.Node(key)
            return self.root

        self.splay(key)

        # if key already existed in the tree
        if self.root.key == key:
            return

        new_node = self.Node(key)
        position = self.find_position(key, self.root)
        if key < position.key:
            position.left = new_node
        else:
            position.right = new_node
        self.splay(key)

        # if key < self.root.key:
        #     new_node.left = self.root.left
        #     new_node.right = self.root
        #     self.root.left = None
        # else:
        #     new_node.right = self.root.right
        #     new_node.left = self.root
        #     self.root.right = None
        # self.root = new_node

    def find_position(self, key, root, prev=None):
        if root is None:
            return prev
        if key < root.key:
            return self.find_position(key, root.left, root)
        else:
            return self.find_position(key, root.right, root)

    def delete(self, key):
        self.splay(key)
        if key != self.root.key:
            raise KeyError('Key not found')

        if self.root.left is None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def search(self, key):
        if self.root is None:
            return None

        self.splay(key)

        # key doesn't exist in the tree
        if self.root.key != key:
            return None

        return self.root.key

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def splay(self, key):
        temp = self.Node(None)
        left = right = temp
        node = self.root
        temp.left = temp.right = None
        while True:
            if key < node.key:
                if node.left is None:
                    break
                if key < node.left.key:
                    node = self.right_rotate(node)
                    if node.left is None:
                        break
                right.left = node
                right = node
                node = node.left
            elif key > node.key:
                if node.right is None:
                    break
                if key > node.right.key:
                    node = self.left_rotate(node)
                    if node.right is None:
                        break
                left.right = node
                left = node
                node = node.right
            else:
                break
        left.right = node.left
        right.left = node.right
        node.left = temp.right
        node.right = temp .left
        self.root = node

    def pre_order_traversal(self, node, res):
        if node:
            res += [node.key]
            res = self.pre_order_traversal(node.left, res)
            res = self.pre_order_traversal(node.right, res)
        return res

    def print(self):
        print(self.pre_order_traversal(self.root, []))


t = SplayTree()
print('insert 3')
t.insert(3)
t.print()
print('insert 10')
t.insert(10)
t.print()
print('insert 4')
t.insert(4)
t.print()
print('insert 11')
t.insert(11)
t.print()
print('search for 3', 'found {}'.format(t.search(3)) if t.search(3) is not None else 'None')
t.print()
print('insert 8')
t.insert(8)
t.print()
print('insert 5')
t.insert(5)
t.print()
print('insert 6')
t.insert(6)
t.print()
print('search for 7', 'found {}'.format(t.search(7)) if t.search(7) is not None else 'None')
print('del 10')
t.delete(10)
t.print()
print('search for 5', 'found {}'.format(t.search(5)) if t.search(5) is not None else 'None')
t.print()
print('del 5')
t.delete(5)
t.print()





