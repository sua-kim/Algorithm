def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

N = int(input())
price_list = [list(map(int, input().split())) for _ in range(N)]
a = list(range(N))
res = 2147483647
while True:
    ok = True
    temp = 0
    for i in range(0, N-1):
        if price_list[a[i]][a[i+1]] == 0:
            ok = False
            break
        temp += price_list[a[i]][a[i+1]]
    if ok and price_list[a[N-1]][a[0]] != 0:
        temp += price_list[a[N-1]][a[0]]
        res = min(temp, res)
    if not next_permutation(a):
        break

print(res)