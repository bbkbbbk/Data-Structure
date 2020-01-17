def radix_helper(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] // exp1)
        count[(index) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    max_val = max(arr)
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max_val / exp > 0:
        radix_helper(arr, exp)
        exp *= 10

    return arr


def radix_sort_str(arr):
    ipt = {}
    for word in arr:
        # total = sum([ord(x) for x in word])  # sort by the sum of all char in word
        # ipt[total] = word
        ipt[ord(word[0])] = word  # sort by the first char -> collision 100%

    return [ipt[x] for x in radix_sort(list(ipt.keys()))]


print(radix_sort([9, 5, 7, 2, 6, 3, 5, 1, 4]))
print(radix_sort_str(['phume', 'bookie', 'neo', 'apple']))