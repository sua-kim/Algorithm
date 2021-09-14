N = int(input())
result = list()
for _ in range(N):
    age, name = input().split()
    result.append((int(age), name))
result.sort(key=lambda x:x[0])
for idx in range(N):
    print(result[idx][0], end=' ')
    print(result[idx][1])