def merge_two_lists(list_left, list_right):
    # Special case: one or both of lists are empty
    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left

    i = j = 0
    list_merged = []  # list to build and return
    len_target = len(list_left) + len(list_right)
    while len(list_merged) < len_target:
        if list_left[i] <= list_right[j]:
            list_merged.append(list_left[i])
            i += 1
        else:
            list_merged.append(list_right[j])
            j += 1

        # If we are at the end of one of the lists we can just append the remainder of the list
        if j == len(list_right):
            list_merged += list_left[i:]
            break
        elif i == len(list_left):
            list_merged += list_right[j:]
            break

    return list_merged


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        mid = len(input_list) // 2
        left, right = input_list[:mid], input_list[mid:]
        return merge_two_lists(merge_sort(left), merge_sort(right))


if __name__ == '__main__':
    print('Array merge sort')
    print(merge_sort([9, 5, 7, 2, 6, 3, 5, 1, 4]))
    print(merge_sort(['phume', 'bookie', 'neo', 'apple']))
