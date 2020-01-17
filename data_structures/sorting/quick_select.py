import random


def quick_select(input_list, k):
    if len(input_list) == 1:
        return input_list[0]

    pivot = random.choice(input_list)
    less = [x for x in input_list if x < pivot]
    equal = [x for x in input_list if x == pivot]
    greater = [x for x in input_list if pivot < x]

    if k <= len(less):
        # kth smallest lies in less
        return quick_select(less, k)
    elif k <= len(less) + len(equal):
        return pivot  # kth smallest to pivot
    else:
        i = k - len(less) - len(equal)
        # kth smallest is ith in greater
        return quick_select(greater, i)


print(quick_select([9, 5, 7, 2, 6, 3, 5, 1, 4], 4))