N, M = map(int, input().split())

a = [0] * M

def recursion(index, start, N, M):
    if index == M:
        print(' '.join(map(str, a)))
        return
    for i in range(start, N+1):
        a[index] = i
        recursion(index+1, i, N, M)

recursion(0, 1, N, M)