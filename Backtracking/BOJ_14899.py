'''
N = int(input())
S_list = [list(map(int, input().split())) for _ in range(N)]

def recursion(index, first, second):
    if index == N:
        if len(first) != N//2 or len(second) != N//2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(N//2):
            for j in range(N//2):
                if i == j:
                    continue
                t1 += S_list[first[i]][first[j]]
                t2 += S_list[second[i]][second[j]]
        diff = abs(t1-t2)
        return diff
    if len(first) > N//2 or len(second) > N//2:
        return -1
    ans = -1 # 최소값이 아직 없는 경우
    t1 = recursion(index+1, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = recursion(index+1, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans

print(recursion(0, [], []))
'''

from itertools import combinations
n = int(input())
s_list = [list(map(int, input().split())) for _ in range(n)]
n_list = [i for i in range(n)]
s = list(combinations(n_list, n//2))

res = 10000
for i in range(len(s)//2):
    start = s[i]
    start_s = 0
    for j in range(n//2):
        member = start[j]
        for k in start:
            start_s += s_list[member][k]
    end = s[-i-1]
    end_s = 0
    for j in range(n//2):
        member = end[j]
        for k in end:
            end_s += s_list[member][k]
    res = min(res, abs(start_s-end_s))

print(res)