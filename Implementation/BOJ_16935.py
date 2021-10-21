def one(array):
    return array[::-1]

def two(array):
    for i in range(len(array)):
        array[i] = array[i][::-1]
    return array

def three(array):
    m = len(array[0])
    result = [[] for _ in range(m)]
    for i in range(len(array)-1,-1,-1):
        for j in range(len(array[0])):
            result[j].append(array[i][j])
    return result

def four(array):
    m = len(array[0])
    result = [[] for _ in range(m)]
    for i in range(len(array)):
        for j in range(m-1, -1, -1):
            result[m-1-j].append(array[i][j])
    return result

def five(array):
    n = len(array)
    m = len(array[0])
    result = [[]*m for _ in range(n)]
    for i in range(n//2, n):
        result[i-n//2] += array[i][0:m//2]
        result[i] += array[i][m//2:m]
    for i in range(0, n//2):
        result[i] += array[i][0:m//2]
        result[i+n//2] += array[i][m//2:m]
    return result

def six(array):
    n = len(array)
    m = len(array[0])
    result = [[] * m for _ in range(n)]
    for i in range(0, n//2):
        result[i] += array[i][m//2:m]
        result[i+n//2] += array[i][0:m//2]
    for i in range(n//2, n):
        result[i-n//2] += array[i][m//2:m]
        result[i] += array[i][0:m//2]
    return result

a, b, r = map(int, input().split())
a_list = [list(map(int, input().split())) for _ in range(a)]
calc_list = list(map(int, input().split()))
for calc in calc_list:
    if calc == 1:
        a_list = one(a_list)
    if calc == 2:
        a_list = two(a_list)
    if calc == 3:
        a_list = three(a_list)
    if calc == 4:
        a_list = four(a_list)
    if calc == 5:
        a_list = five(a_list)
    if calc == 6:
        a_list = six(a_list)
for arr in a_list:
    print(' '.join(map(str, arr)))