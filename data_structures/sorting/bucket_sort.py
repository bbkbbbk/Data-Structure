from quick_sort import quick_sort


def bucket_sort(input_list):
    # 10 slots, each slot's size is 0.1
    slot_num = 10
    # create a bucket for 10 slots
    bucket = [[] for _ in range(slot_num)]

    for j in input_list:
        # Put array elements in different buckets 0.23 -> bucket[2] 0.89 -> bucket[8]
        index = int(slot_num * j)
        bucket[index].append(j)

    # Sort individual buckets using other sorting algo to help
    bucket = [quick_sort(x) for x in bucket]

    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            # put elem in bucket back to original list
            input_list[k] = bucket[i][j]
            k += 1
    return input_list


def bucket_sort_str(input_list):
    slot_num = 57
    bucket = [[] for _ in range(slot_num)]

    for j in input_list:
        index = ord(j[0]) % ord('A')
        bucket[index].append(j)

    bucket = [quick_sort(x) for x in bucket]

    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            input_list[k] = bucket[i][j]
            k += 1
    return input_list


print(bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]))
print(bucket_sort_str(['phume', 'Bookie', 'Neo', 'apple']))