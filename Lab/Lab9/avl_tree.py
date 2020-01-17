
'''
the problem of bst is that its height is not under control
the time complexity min = logn max = n depends on the height and the order of elem when insert
'''
class AVL_Tree:
    class Node:
        __slots__ = 'value', 'parent', 'left', 'right', 'height'

        def __init__(self, v, p=None, l=None, r=None):
            self.value = v
            self.parent = p
            self.left = l
            self.right = r
            self.height = 1

    def __init__(self):
        self.root = None
        self.size = 0

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return self.Node(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.value:
            print('left, left')
            return self.right_rotate(root)

        if balance < -1 and key > root.right.value:
            print('right, right')
            return self.left_rotate(root)

        if balance > 1 and key > root.left.value:
            print('left, right')
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.value:
            print('right, left')
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        self.size += 1
        return root

    def pre_order_traversal(self, root, res=[]):
        if not root:
            return

        res += [root.value]
        self.pre_order_traversal(root.left, res)
        self.pre_order_traversal(root.right, res)
        return res

    def num_children(self, p, num=0): 
        if p is not None:
            if p.left is not None:
                num += 1
                self.num_children(p.left, num)
            if p.right is not None:
                num += 1
                self.num_children(p.right, num)
        return num

    def find_median(self, root, prev=None):
        if prev is None:
            self.root = root
        if root is None:
            if self.size % 2 == 0:
                print('Median is:', (prev.value + self.root.value) / 2)
            else:
                print('Median is:', prev.value)
            return
        num_left = self.num_children(root.left)
        num_right = self.num_children(root.right)
        if num_left > num_right:
            self.find_median(root.left, root)
        else:
            self.find_median(root.right, root)

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.find_min(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def find_min(self, root):
        if root is None or root.left is None:
            return root

        return self.find_min(root.left)




tree = AVL_Tree()
root = None

root = tree.insert(root, 10)
root = tree.insert(root, 20)
root = tree.insert(root, 30)
root = tree.insert(root, 40)
root = tree.insert(root, 50)
root = tree.insert(root, 25)
print('Preorder traversal:', tree.pre_order_traversal(root, []))
# tree.find_median(root)
root = tree.delete(root, 20)
root = tree.delete(root, 40)
print('Preorder traversal:', tree.pre_order_traversal(root, []))

