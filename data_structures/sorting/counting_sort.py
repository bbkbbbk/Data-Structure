'''
Counting sort is the wrong sorting algorithm for string. The counting sort algorithm is designed to sort integer
values that are in a fixed range, so it can't be applied to sort strings.
'''

def count_sort(input_list):
    min_val = min(input_list)
    max_val = max(input_list)

    count = [0 for _ in range(min_val, max_val + 1)]
    output = [0 for _ in range(min_val, max_val + 1)]

    for i in range(len(count)):
        count[input_list[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(input_list) - 1, -1, -1):
        output[count[input_list[i] - min_val] - 1] = input_list[i]
        count[input_list[i] - min_val] -= 1

    return output


def count_sort_char(input_list):
    # output character array that will have sorted arr
    output = [0 for i in range(256)]
    # create a count array to store count of each characters
    count = [0 for i in range(256)]

    for i in input_list:
        # count of each character
        count[ord(i)] += 1

    for i in range(256):
        # change count[i] so that count[i] now contains actual position of character
        count[i] += count[i - 1]

    for i in range(len(input_list)):
        # build the output character array
        output[count[ord(input_list[i])] - 1] = input_list[i]
        count[ord(input_list[i])] -= 1

    output = [x for x in output if x is not 0]
    return output


print(count_sort([9, 5, 7, 2, 6, 3, 5, 1, 4]))
print(count_sort_char(['a', 'c', 'e', 's']))
