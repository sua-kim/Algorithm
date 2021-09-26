N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()
a = [0] * M
def recursion(index, start, N, M):
    if index == M:
        print(' '.join(map(str, a)))
        return
    for i in range(start, N):
        a[index] = N_list[i]
        recursion(index+1, i, N, M)
        a[index] = 0

recursion(0, 0, N, M)