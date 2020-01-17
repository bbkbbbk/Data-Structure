def norm(n, p=2):
    result = sum([pow(i, p) for i in n])
    return pow(result, 1/p)


with open('testcase1-1.txt') as f:
    for line in f:
        line = line.strip('\n').split()
        line = list(map(int, line))
        print(line, 'defalut norm:', norm(line))
        print(line, '3-norm:', norm(line, 3))
        print()



