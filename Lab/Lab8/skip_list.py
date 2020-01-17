import random

class Node:
    __slots__ = 'key', 'value', 'next', 'below'

    def __init__(self, key, value, next=None, below=None):
        self.key = key
        self.value = value
        self.next = next
        self.below = below

    def __eq__(self, other):
        return self.key == other.key

    def __gt__(self, other):
        if self.key == None:
            return False
        elif other.key == None:
            return True
        return self.key > other.key

    def __ge__(self, other):
        if self.key == None:
            return False
        elif other.key == None:
            return True
        return self.key >= other.key

    def __lt__(self, other):
        if self.key == None:
            return True
        elif other.key == None:
            return False
        return self.key < other.key

    def __le__(self, other):
        if self.key == None:
            return True
        elif other.key == None:
            return False
        return self.key <= other.key

class SortedLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def add(self, node):
        current = start = self.head

        # check duplication
        if node.key is not None:
            while start.next:
                if start.key == node.key:
                    raise KeyError('Duplicate Key')
                start = start.next

        new_node = node
        if current is None:
            self.head = new_node
            return new_node

        if current > new_node:
            new_node.next = current
            self.head = new_node
            return new_node

        while current.next is not None:
            if current.next > new_node:
                break
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def items(self):
        current = self.head
        while current:
            yield current.key, current.value
            current = current.next

class SkipList:
    def __init__(self, max_layer=8):
        self.max_layer = max_layer
        self.layers = [SortedLinkedList()]
        self.layers[0].add(Node(None, None))

    def generate_height(self):
        return random.randint(2, self.max_layer)

    def insert(self, key, value):
        below = None
        num_layers = len(self.layers)

        height = self.generate_height()
        if height > num_layers:
            for i in range(num_layers, height):
                self.layers.append(SortedLinkedList())
                new_head = Node(None, None)
                new_head.below = self.layers[i - 2].head
                self.layers[i].add(new_head)
        for i in range(height):
            new_node = Node(key, value)
            self.layers[i].add(new_node)
            new_node.below = below
            below = new_node

    def skip_search(self, key):
        p = self.layers[len(self.layers) - 1].head
        while p.below:
            p = p.below
            while p.next and key >= p.next.key:
                p = p.next
        if p.key == key:
            return p
        else:
            raise KeyError('Key not found')

    def update(self, key, new_value):
        for layer in self.layers:
            for node in layer:
                if node.key == key:
                    node.value = new_value

    def print(self):
        for i in range(len(self.layers))[::-1]:
            print('layer: {}'.format(i), end='\t')
            for node in self.layers[i]:
                print('({}, {})'.format(node.key, node.value), end=' ')
            print()

    def __getitem__(self, key):
        item = self.skip_search(key)
        if item is None or item.key is None:
            raise KeyError('Key not found')
        else:
            return item.value

s = SkipList()
s.insert(4, 1)
s.insert(3, 2)
s.insert(1, 3)
s.insert(8, 4)
s.insert(9, 5)
s.insert(10, 6)
s.insert(5, 7)
s.insert(6, 8)
s.insert(7, 9)
## Will raise error
# s.insert(4, 3)

print('Search key 5:')
item = s.skip_search(5)
print('({}, {})'.format(item.key, item.value))
## Will raise error
# print('Search key 0:')
# item = s.skip_search(0)
# print('({}, {})'.format(item.key, item.value))

print('================================================')
print('Get value of 9:', s[9])
## Will raise error
# print('Get value of 0:', s[0])

print('================================================')
s.print()

print('================================================')
print('update value of 3 to 99')
s.update(3, 99)
s.print()








