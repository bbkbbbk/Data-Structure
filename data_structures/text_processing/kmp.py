def compute_kmp_fail(pattern):
    m = len(pattern)
    i = 1
    j = 0
    fail = [0] * m
    while i < m:
        if pattern[i] == pattern[j]:
            fail[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            fail[j] = fail[j - 1]
            j = 0
        else:
            i += 1

    return fail


def find_kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0

    i = j = 0
    fail = compute_kmp_fail(pattern)
    print('Fail:', fail)

    while i < n:
        if text[i] == pattern[j]:
            if j == m - 1:
                return i - m + 1
            i += 1
            j += 1
        elif j > 0:
            j = fail[j - 1]
        else:
            i += 1

    return False

print(find_kmp('abacaabadcabacabaabb', 'abacab'))