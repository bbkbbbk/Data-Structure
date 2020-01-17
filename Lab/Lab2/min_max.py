def min_max(lst, min = None, max = None):
    # for last call whem there's no element in list anymore
    if len(lst) == 0:
        return min, max

    # for 1st call initialize value for min max
    if min == None and max == None:
        min, max = lst[0], lst[0]
    elif lst[0] < min:
        min = lst[0]
    elif lst[0] > max:
        max = lst[0]
    # check next element
    return min_max(lst[1:], min, max)

print(min_max([9, 4, 2, 6, 1, 0, 22]))
print(min_max((1, 6, 9, 88, 5, 3, -5)))