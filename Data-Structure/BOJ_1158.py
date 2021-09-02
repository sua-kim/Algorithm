N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

temp = 0
res = []
while arr:
    temp += K-1
    temp %= len(arr)
    value = arr[temp]
    res.append(value)
    arr.remove(value)
print('<', end='')
print(', '.join(map(str, res)), end='')
print('>')