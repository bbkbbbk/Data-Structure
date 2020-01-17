from time import time
from itertools import permutations
from copy import deepcopy

def permute(left, right = []):
    if len(left) == 0:
        print(right)
    else:
        for i in left:
            temp = deepcopy(left)
            temp.remove(i)
            permute(temp, right + [i])


# O(n!)
start = time()
permute([1, 2, 3])
end = time()
print("Bookie's algo:", end - start)

# start = time()
# list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# end = time()
# print("Itertools:", end - start)
