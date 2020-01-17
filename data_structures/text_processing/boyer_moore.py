def find_boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    # text and pattern index
    i = j = m - 1
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            i = i + m - min(j, 1 + text.rfind(text[i]))
            j = m - 1
    return False

print(find_boyer_moore('abacaabadcabacabaabb', 'abacab'))