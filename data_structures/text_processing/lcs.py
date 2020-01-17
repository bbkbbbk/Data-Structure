def LCS_dynamic(a, b):
    ab = [[0] * len(b)] * len(a)
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                ab[i][j] = 1 + ab[i - 1][j - 1]
            else:
                ab[i][j] = max(ab[i - 1][j], ab[i][j - 1])
    print('Table:')
    print(*ab, sep="\n")

    return ab[len(a) - 1][len(b) - 1]


a = ' bd'
b = ' abcd'
print('LCS:', LCS_dynamic(a, b))