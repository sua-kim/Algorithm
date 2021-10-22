import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
c = [False] * (N+1)
a = [0] * M

def recursion(index, N, M):
    if index == M:
        print(' '.join(map(str, a))+'\n')
        return
    else:
        for i in range(1, N+1):
            if c[i]:
                continue
            c[i] = True
            a[index] = i
            recursion(index+1, N, M)
            c[i] = False

recursion(0, N, M)


'''
from itertools import permutations

n, m = map(int, input().split())
n_list = [i for i in range(1, n+1)]
p_list = list(permutations(n_list, m))
for p in p_list:
    print(' '.join(map(str, p)))
'''