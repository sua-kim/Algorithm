N = int(input())
result = list()
for _ in range(N):
    result.append(int(input()))
result.sort()
for num in result:
    print(num)