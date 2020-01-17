import random


def quick_sort(input_list):
    if len(input_list) < 1:
        return input_list

    less = []
    equal = []
    greater = []
    # select pivot at random
    pivot = random.choice(input_list)
    # median pivot works only int
    # pivot = (input_list[0] + input_list[-1] + input_list[len(input_list) // 2]) // 3

    for x in input_list:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        elif x > pivot:
            greater.append(x)

    return quick_sort(less) + equal + quick_sort(greater)

if __name__ == '__main__':
    print(quick_sort([6, 2, 5, 7, 8, 3, 4, 1]))
    print(quick_sort(['vop', 'boo', 'obo', 'keo']))
