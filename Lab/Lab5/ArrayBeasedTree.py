class BinaryTree:
    def __init__(self):
        self.size = 0;
        self.tree = [None]

    def __len__(self):
        return self.size;

    # set root fot tree
    def root(self):
        if len(self.tree) != 0:
            return self.tree[0]
        return None

    # check if position p is root
    def is_root(self, p):
        return p == 0

    # return the position of left node of position p
    def left(self, p):
        if 2 * p + 1 > len(self.tree) - 1:
            return None
        return self.tree[2 * p + 1]

    # return the position of right node of position p
    def right(self, p):
        if 2 * p + 2 > len(self.tree) - 1:
            return None
        return self.tree[2 * p + 2]

    # return the position of parent of position p
    def parent(self, p):
        return self.tree[(p-1) // 2]

    # add left node to node in the position p to have value of e
    def add_left(self, p, e):
        # if there is no elem in tree -> e is the root of tree
        if self.size == 0:
            self.tree[0] = e
            self.size += 1
        else:
            # the position of e
            index = 2 * p + 1

            # if the position of e is bigger than the len of self.tree then self.tree need to resize
            if index > len(self.tree) - 1:
                self.resize(index + 1)
            # check if at the position of e has elem already exist or not
            if self.tree[index] is not None:
                print('value exists')
                return False

            self.size += 1
            self.tree[index] = e

    # add right node to node in the position p to have value of e
    def add_right(self, p, e):
        # if there is no elem in tree -> e is the root of tree
        if self.size == 0:
            self.tree[0] = e
            self.size += 1
        else:
            # the position of e
            index = 2 * p + 2

            # if the position of e is bigger than the len of self.tree then self.tree need to resize
            if index > len(self.tree) - 1:
                self.resize(index + 1)
            # check if at the position of e has elem already exist or not
            if self.tree[index] is not None:
                print('value exists')
                return False

            self.size += 1
            self.tree[index] = e

    def resize(self, n):
        old = self.tree
        self.tree = [None] * n
        for i in range(len(old)):
            self.tree[i] = old[i]

    def num_children(self):
        count = 0
        for i in self.tree:
            if i is not None:
                count += 1
        return count

    def is_leaf(self, p):
        left = 2 * p + 1
        right = 2 * p + 2
        if left > len(self.tree) - 1 and right > len(self.tree) - 1:
            return True
        if self.tree[left] is not None:
            return False
        if self.tree[right] is not None:
            return False
        return True

    def set(self, p, e):
        if p > len(self.tree) - 1:
            self.resize(p)
        self.tree[p] = e

    def attach(self, p, t1, t2):
        if not self.is_leaf(p):
            print('position must be leaf')
            return False
        if not type(self) is type(t1) is type(t2):
            print('Tree type must be the same')
            return False
        if p > len(self.tree) - 1:
            print('index out of range')
            return False
        self.size += t1.size

        self.resize(len(self.tree) + len(t1.tree))

        # self.add_right(p, t2)

    def remove(self, p):
        if p > len(self.tree) - 1:
            print('index out of range')
            return None

        if self.left(p) is not None and self.right(p) is not None:
            print('error p has 2 children')
            return None

        if self.left(p) is not None:
            new_value = self.remove(2 * p + 1)
        elif self.right(p) is not None:
            new_value = self.remove(2 * p + 2)
        else:
            temp = self.tree[p]
            self.tree[p] = None
            return temp

        temp = self.tree[p]
        self.tree[p] = new_value
        return temp

t = BinaryTree()
t.add_left(0, 0)

t.add_left(0, 1)
t.add_right(0, 2)

t.add_left(1, 3)
t.add_right(1, 4)

t.add_left(2, 5)
t.add_right(2, 6)
print('len of tree:', len(t))
print('number of children:', t.num_children())
print('is p = 0 is root', t.is_root(0))
print('is p = 5 is root', t.is_root(5))

print('left node for node at p = 2:', t.left(2))
print('left node for node at p = 5:', t.left(5))
print('right node for node at p = 2:', t.right(1))
print('right node for node at p = 2:', t.right(3))
print('is p = 0 is leaf:', t.is_leaf(0))
print('is p = 2 is leaf:', t.is_leaf(2))
print('is p = 3 is leaf:', t.is_leaf(3))
print('parent of p = 1: ', t.parent(1))
print('parent of p = 3: ', t.parent(3))
print('parent of p = 6: ', t.parent(6))
print(t.tree)

print('set p = 6 to 9')
t.set(6, 9)
print(t.tree)

print('remove 1')
t.remove(1)
print(t.tree)

t.add_right(6, 88)
print(t.tree)
print('remove 6')
t.remove(6)
print(t.tree)
















# print('attach p = 5 with t1, t2')
# # [0, 1, 2]
# t1 = BinaryTree()
# t1.add_left(0, 0)
# t1.add_left(0, 1)
# t1.add_right(0, 2)
#
# t2 = BinaryTree()
# t2.add_left(0, 0)
# t2.add_left(0, 1)
# t2.add_right(0, 2)
# t.attach(6, t1, t2)
# print(t.tree)

