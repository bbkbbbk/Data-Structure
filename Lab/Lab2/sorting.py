import matplotlib.pyplot as plt
import random
from time import time

def foo(n):
    count = 0
    for i in range(n//2, n):
        j = 1
        while j + n/2 <= n:
            k = 1
            while k <= n:
                count = count + 1
                k = k * 2
            j = j + 1

plt.title('Python sorting')
plt.ylabel('Time')
plt.xlabel('Number of input')

time_used = []
num = []

for i in range(1, 1000, 20):
    start = time()
    foo(i)
    end = time()
    time_used.append(end-start)
    num.append(i)
#
# for i in range(1, 1000, 50):
#     # create list size i with random number
#     lst = random.sample(range(1, 1000), i)
#
#     # timer
#     start = time()
#     lst.sort()
#     end = time()
#
#     # add to list for plotting
#     time_used.append(end - start)
#     num.append(i)


plt.plot(num, time_used)
plt.show()