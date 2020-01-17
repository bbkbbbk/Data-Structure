# Linked list version
class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.last = None  # for quick sort
        self.sorted = None # for insertion sort
        self.size = 0

    def add(self, v):
        new_node = self.Node(v)

        if self.head is None:
            self.head = self.last = new_node
            return

        self.last.next = new_node
        self.last = new_node

    def sorted_node(self, a, b):
        result = None

        if a is None:
            return b

        if b is None:
            return a

        if a.value <= b.value:
            result = a;
            result.next = self.sorted_node(a.next, b)
        else:
            result = b;
            result.next = self.sorted_node(a, b.next)

        return result

    def _merge_helper(self, head):  # find middle function
        if head is None:
            return head

        slow = fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self._merge_helper(head)
        middle_next = middle.next

        middle.next = None
        left = self._merge_sort(head)
        right = self._merge_sort(middle_next)

        sorted_list = self.sorted_node(left, right)

        return sorted_list

    def merge_sort(self):
        self.head = self._merge_sort(self.head)

    def _quick_helper(self, start, end):  # partition function
        if start == end or start is None or end is None:
            return start

        pivot_prev = curr = start
        pivot = end.value

        # iterate till one before the end, no need to iterate till the end bc end is pivot
        while start != end:
            if start.value < pivot:
                pivot_prev = curr  # keep track of last modified item
                curr.value, start.value = start.value, curr.value
                curr = curr.next
            start = start.next
        # swap the position of curr ie next suitable index and pivot
        temp = curr.value
        curr.value = pivot
        end.value = temp
        # return one previous to curr bc curr is noe pointing to pivot
        return pivot_prev

    def _quick_sort(self, start, end):
        if start == end:
            return
        # split list and partition recurse
        pivot_prev = self._quick_helper(start, end)
        self._quick_sort(start, pivot_prev)
        # if pivot is picked and moved to the start,
        # that means start and pivot is same. so pick from next pivot
        if pivot_prev is not None and pivot_prev == start:
            self._quick_sort(pivot_prev.next, end)
        # if pivot is in between of the list, start from next of pivot
        # since we have pivot_prev, so we move 2 nodes
        elif pivot_prev is not None and pivot_prev.next is not None:
            self._quick_sort(pivot_prev.next.next, end)

    def quick_sort(self):
        temp = self.head
        self._quick_sort(self.head, self.last)
        self.head = temp

    def _insertion_helper(self, node):  # function to insert a node in a list.
        if self.sorted is None or self.sorted.value >= node.value:
            node.next = self.sorted
            self.sorted = node
        else:
            curr = self.sorted
            while curr.next is not None and curr.next.value < node.value:
                curr = curr.next

            node.next = curr.next
            curr.next = node

    def insertion_sort(self):
        self.sorted = None
        curr = self.head

        # traverse the given linked list and insert every node to sorted
        while curr is not None:
            next = curr.next  # store next for next iteration
            self.insertion_helper(curr)  # insert curr in sorted linked list
            curr = next
        self.head = self.sorted

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print()


print('\nLinked list merge sort')
l = LinkedList()
l.add(15)
l.add(10)
l.add(5)
l.add(20)
l.add(2)
l.add(3)
print('Before sort')
l.print()
print('After sort')
# l.merge_sort()
# l.quick_sort()
l.insertion_sort()
l.print()