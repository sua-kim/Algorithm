def recursion(n):
    k = n + sum(map(int, list(str(n))))
    return k
dn = []
for i in range(1, 10001):
    temp = recursion(i)
    if temp > 10000:
        continue
    dn.append(temp)
for i in range(1, 10001):
    if i not in dn:
        print(i)