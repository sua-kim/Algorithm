from itertools import permutations
n = int(input())
n_list = list(map(int, input().split()))

def solve(a):
    summation = 0
    for i in range(0, len(a)-1):
        summation += abs(a[i]-a[i+1])
    return summation

res = 0
for i in list(permutations(n_list, n)):
    res = max(res, solve(i))
print(res)
