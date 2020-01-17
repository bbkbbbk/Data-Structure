from Lab3 import ArrayBasedDS
ArrayStack = ArrayBasedDS.ArrayStack

def postfix(ipt):
    ipt = ipt.split()
    stack = ArrayStack()
    for item in ipt:
        if item not in ['+', '-', '*', '/']:
            stack.push(item)
        else:
            right = stack.pop()
            left = stack.pop()
            str_exp = '{} {} {}'.format(left, item, right)
            print(str_exp)
            stack.push(eval(str_exp))
            print(stack.getData())

postfix('5 2 + 8 3 - * 4 /')