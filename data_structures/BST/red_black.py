from binary_search_tree import BinarySearchTree


RED = 'red'
BLACK = 'black'


class RedBlackTree(BinarySearchTree):
    class Node:
        def __init__(self, k, p=None, c=RED):
            self.key = k
            self.parent = p
            self.color = c
            self.left = self.right = None
        
        def is_left(self):
            return self is self.parent.left
        
        def has_red_child(self):
            return (self.left is not None and self.left.color is RED) or \
                   (self.right is not None and self.right.color is RED)
        
        def uncle(self):
            # if no parent or grandparent then there is no uncle
            if self.parent is None or self.parent.parent is None:
                return None
            
            if self.parent.is_left():
                return self.parent.parent.right  # uncle is on the right
            else:
                return self.parent.parent.right  # uncle is on the left
        
        def get_sibling(self):
            if self.parent is None:
                return None
            
            if self.is_left():
                return self.parent.right
            return self.parent.left
        
        def move_down(self, p):  # moves node down and moves given node in its place
            if self.parent is not None:
                if self.is_left():
                    self.parent.left = p
                else:
                    self.parent.right = p
            
            p.parent = self.parent
            self.parent = p
            
    def __init__(self):
        self.root = None
        self.size = 0
        
    def left_rotate(self, node):
        parent = node.right
        
        if node is self.root:
            self.root = parent
            
        node.move_down(parent)
        node.right = parent.left
        
        if parent.left is not None:
            parent.left.parent = node
        
        parent.left = node
        
    def right_rotate(self, node):
        parent = node.left
        
        if node is self.root:
            self.root = parent
            
        node.move_down(parent)
        node.left = parent.right
        
        if parent.right is not None:
            parent.right.parent = node
            
        parent.right = node
        
    def swap_color(self, x, y):
        x.color, y.color = y.color, x.color
    
    def swap_key(self, x, y):
        x.key, y.key = y.key, x.key
        
    def fix_red_red(self, node):
        if node is self.root:
            node.color = BLACK
            return  # if node is root color it black and return

        parent = node.parent
        uncle = node.uncle()
        grandparent = parent.parent

        if parent.color is not BLACK:
            if uncle is not None and uncle.color is RED:  # uncle red, perform recoloring and recurse
                parent.color = BLACK
                uncle.color = BLACK
                grandparent.color = RED
                self.fix_red_red(grandparent)
            else:  # Else perform LR, LL, RL, RR
                if parent.is_left():
                    if node.is_left():
                        self.swap_color(parent, grandparent)  # left right
                    else:
                        self.left_rotate(parent)
                        self.swap_color(node, grandparent)
                    self.right_rotate(grandparent)  # left left and left right
                else:
                    if node.is_left():  # right right
                        self.right_rotate(parent)
                        self.swap_color(node, grandparent)
                    else:
                        self.swap_color(parent, grandparent)
                    self.left_rotate(grandparent)  # right eight and right left

    def fix_black_black(self, node):
        if node is self.root:
            return

        sibling = node.get_sibling()
        parent = node.parent

        if sibling is None:  # no sibling double black push up
            self.fix_black_black(parent)
        else:
            if sibling.color is RED:
                parent.color = RED
                sibling.color = BLACK
                if sibling.is_left():
                    self.right_rotate(parent)
                else:
                    self.left_rotate(parent)
                self.fix_black_black(node)
            else:
                if sibling.has_red_child():
                    if sibling.left is not None and sibling.left.color is RED:  # at least 1 red children
                        if sibling.is_left():  # left left
                            sibling.left.color = sibling.color
                            sibling.color = parent.color
                            self.right_rotate(parent)
                        else:  # right left
                            sibling.left.color = parent.color
                            self.right_rotate(sibling)
                            self.left_rotate(parent)
                    else:
                        if sibling.is_left():  # left right
                            sibling.right.color = parent.color
                            self.left_rotate(sibling)
                            self.right_rotate(parent)
                        else:  # right right
                            sibling.right.color = sibling.color
                            sibling.color = parent.color
                            self.left_rotate(parent)
                    parent.color = BLACK
                else:  # 2 black children
                    sibling.color = RED
                    if parent.color is BLACK:
                        self.fix_black_black(parent)
                    else:
                        parent.color = BLACK

    def find_replace(self, node):  # find node that replaces a deleted node in BST
        # when node is leaf
        if node.left is None and node.right is None:
            return None
        # when node have 2 children
        if node.left is not None and node.right is not None:
            return self.find_min(node.right)
        # when node is a single child
        if node.left is not None:
            return node.left
        else:
            return node.right

    def delete(self, key):
        if self.root is None:
            return  # tree is empty

        node = self._search(self.root, key)

        if node.key != key:
            print('Delete key {}: Not found'.format(key))
            return

        self._delete(node)
        self.size -= 1
        print('Delete key {}: Succeed'.format(key))

    def _delete(self, node):
        u = self.find_replace(node)

        is_both_black = (u is None or u.color is BLACK) and (node.color is BLACK)
        parent = node.parent

        if u is None:  # if u is none so node is leaf
            if node is self.root:
                self.root = None  # node is root making root none
            else:
                if is_both_black:  # node is leaf -> fix black black at node
                    self.fix_black_black(node)
                else:  # node and u is red
                    if node.get_sibling() is not None:
                        node.get_sibling().color = RED  # sibling is not none then make it red
                # delete node from the tree
                if node.is_left():
                    parent.left = None
                else:
                    parent.right = None
                return

        if node.left is None or node.right is None:  # node has 1 child
            if node is self.root:  # node is root , assign value of u to node
                node.key = u.key
                node.left = node.right = None
            else:  # detach node from tree and move u up
                if node.is_left():
                    parent.left = u
                else:
                    parent.right = u
                u.parent = parent

                if is_both_black:  # node and u are both black -> fix black black violation
                    self.fix_black_black(u)
                else:
                    u.color = BLACK  # u or node is red, color u black
            return
        # node has 2 children, swap value with successor and recurse
        self.swap_key(u, node)
        self.delete(u)

    def insert(self, key):
        new_node = self.Node(key)
        self.size += 1

        if self.root is None:
            new_node.color = BLACK
            self.root = new_node
        else:
            parent = self._search(self.root, key)
            if parent.key == key:
                return  # key already exist

            new_node.parent = parent

            if key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node
            # fix red red violation if exist
            self.fix_red_red(new_node)


if __name__ == '__main__':
    tree = RedBlackTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(25)
    tree.in_order_traversal()

    tree.delete(20)
    tree.delete(40)
    tree.in_order_traversal()

    tree.search(20)
    tree.search(30)
