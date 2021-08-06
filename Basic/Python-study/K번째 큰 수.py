N, K = map(int, input().split())
card = list(map(int, input().split()))

a = set()

'''
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            a.add(card[i]+card[j]+card[k])
'''

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            a.add(card[i]+card[j]+card[k])

print(sorted(list(a), reverse=True)[K-1])
