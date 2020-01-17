def insertion_sort(input_list):
    n = len(input_list)

    for i in range(1, n):
        key = input_list[i]

        while i > 0 and input_list[i - 1] > key:
            input_list[i] = input_list[i - 1]
            i -= 1
            input_list[i] = key

    return input_list


if __name__ == '__main__':
    print(insertion_sort([9, 5, 7, 2, 6, 3, 5, 1, 4]))
    print(insertion_sort(['vop', 'boo', 'obo', 'keo']))
