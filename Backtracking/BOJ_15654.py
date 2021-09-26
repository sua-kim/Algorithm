N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()
a = [0] * M
def recursion(index, M):
    if index == M:
        print(' '.join(map(str, a)))
        return
    for num in N_list:
        if num in a:
            continue
        a[index] = num
        recursion(index+1, M)
        a[index] = 0

recursion(0, M)