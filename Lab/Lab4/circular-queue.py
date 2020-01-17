from Lab4 import ArrayBasedDS
ArrayQueue = ArrayBasedDS.ArrayQueue

class CircularQueue(ArrayQueue):
    def __init__(self):
        super().__init__()

    def front(self):
        return super().first()

    def rotate(self):
        self.enqueue(self.dequeue())

cq = CircularQueue()

print('Before:')
cq.enqueue(9)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(7)
print(cq)

print('\nAfter dequeue:')
cq.dequeue()
print(cq)

print('\nLength:', len(cq))

print('\nFront:', cq.front())

print('\nIs empty:', cq.is_empty())

print('\nAfter rotate:')
cq.rotate()
print(cq)


