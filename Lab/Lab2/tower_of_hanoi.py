total = [0]

def tower(n, beg, aux, end):
    if n == 1:
        print(beg, '-->', end)
        total[0] += 1
    else:
        tower(n - 1, beg, end, aux)
        tower(1, beg, aux, end)
        tower(n - 1, aux, beg, end)

tower(8, 'A', 'B', 'C')
print(total)