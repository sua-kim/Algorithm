row, column = map(int, input().split())
a = [False] * row
b = [False] * column
c_list = [list(input()) for _ in range(row)]
for i in range(row):
    for j in range(column):
        if c_list[i][j] == 'X':
            a[i] = True
            b[j] = True

print(max(a.count(False),b.count(False)))