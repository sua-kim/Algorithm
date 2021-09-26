N, M = map(int, input().split())

a = [0] * M

def recursion(index, count, N, M):
    if count == M:
        print(' '.join(map(str, a)))
        return
    for i in range(1, N+1):
        a[index] = i
        recursion(index+1, count+1, N, M)

recursion(0, 0, N, M)
