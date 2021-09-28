while True:
    N, *arr = list(map(int, input().split()))
    if N == 0:
        break
    a = [0] * 6
    def recursion(index, start, N):
        if index >= 6:
            print(' '.join(map(str, a)))
            return
        for i in range(start, N):
            a[index] = arr[i]
            recursion(index+1, i+1, N)
            a[index] = 0
    recursion(0, 0, N)
    print()