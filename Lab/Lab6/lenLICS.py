class LinkedList:
    class Node:
        __slots__ = 'value', 'next'
        def __init__(self, v, n=None):
            self.value = v
            self.next = n

    def __init__(self):
        self.start = None
        self.current = None

    def add(self, value):
        new_node = self.Node(value)
        if self.start is None:
            self.start = new_node
            self.current = self.start
        else:
            self.current.next = new_node
            self.current = new_node

    def traverse_list(self):
        if self.start:
            n = self.start
            while n:
                print(n.value, end=' ')
                n = n.next

    def lenLICS(self):
        longest = count = 1
        temp = self.start
        while temp.next is not None:
            if temp.value <= temp.next.value:
                count += 1
            else:
                if longest < count:
                    longest = count
                count = 1
            temp = temp.next
        return longest

list1 = LinkedList()
list1.add(3)
list1.add(6)
list1.add(2)
list1.add(8)
list1.add(12)
list1.add(7)
list1.add(1)
list1.add(4)
print(list1.lenLICS())

list2 = LinkedList()
list2.add(-1)
list2.add(3)
list2.add(-5)
list2.add(-2)
list2.add(4)
list2.add(10)
list2.add(0)
list2.add(11)
print(list2.lenLICS())
