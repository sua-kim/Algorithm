E, S, M = map(int, input().split())

e, s, m = 1, 1, 1

for i in range(1, 7981):
    if e == E and s == S and m == M:
        print(i)
    e += 1
    s += 1
    m += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
