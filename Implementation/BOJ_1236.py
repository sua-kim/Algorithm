N, M = map(int, input().split())
row = set()
column = set()

for i in range(N):
    M_list = list(input())
    for j in range(M):
        if M_list[j] == 'X':
            row.add(j)
            column.add(i)

print(max(M-len(row), N-len(column)))

