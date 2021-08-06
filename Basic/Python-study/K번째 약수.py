N, K = map(int, input().split())
'''
divisor = []

for i in range(1, N + 1):
    if N % i == 0:
        divisor.append(i)

if len(divisor) < K:
    print(-1)
else:
    print(divisor[K-1])
'''

cnt = 0

for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        break
else:
    print(-1)
