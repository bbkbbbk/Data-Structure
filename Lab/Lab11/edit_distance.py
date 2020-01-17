'''
The Levenshtein Distance
 ------------------
| replace | insert |
 ------------------  -> then take the min value from 3 of them if same the val is min else val + 1
|  delete | u here |
 ------------------
 In the lab can use only del and insert
'''


def edit_distance(str1, str2):
    n = len(str1) + 1
    m = len(str2) + 1
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if x == 0:
                matrix[x][y] = y
            elif y == 0:
                matrix[x][y] = x
            elif str1[x - 1] == str2[y - 1]:
                # no operation and choose val in diag
                matrix[x][y] = matrix[x - 1][y - 1]
            else:
                val = min(
                    matrix[x - 1][y],
                    # replace becomes 2 operations (del and insert)
                    matrix[x - 1][y - 1] + 1,
                    matrix[x][y - 1]
                ) + 1   # the number of operation increase
                matrix[x][y] = val
    str2 = ' ' + str2
    print(list(' ' + str1))
    for i in range(len(matrix)):
        print(str2[i], matrix[i])

    return matrix[n - 1][m - 1]


print(edit_distance('abba', 'abbb'))
