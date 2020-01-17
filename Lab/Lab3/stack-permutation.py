from Lab3 import ArrayBasedDS
from copy import deepcopy
ArrayStack = ArrayBasedDS.ArrayStack

def permute(stack):
    left, right = stack.pop()
    if len(left) == 0:
        print(right)
    else:
        for i in left:
            temp = deepcopy(left)
            temp.remove(i)
            elem = (temp, right + [i])
            stack.push(elem)
            permute(stack)

pandas = ([1, 2, 3], [])
stack = ArrayStack()
stack.push(pandas)
permute(stack)


