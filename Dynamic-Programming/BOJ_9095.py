# 브루트포스를 사용해서 풀이하는 법
T = int(input())
'''
def recursion(index, n):
    if sum(arr) == n:
        global count
        count += 1
        return
    if index >= n:
        return
    for i in range(1, 4):
        arr[index] = i
        recursion(index+1, n)
        arr[index] = 0

for _ in range(T):
    n = int(input())
    count = 0
    arr = [0] * n
    recursion(0, n)
    print(count)
'''

# 다른 재귀 함수 사용하는 경우
def recursion1(count, sum, n):
    if sum > n:
        return 0
    if sum == n:
        return 1
    now = 0
    for i in range(1, 4):
        now += recursion1(count+1, sum+i, n)
    return now

for _ in range(T):
    n = int(input())
    result = recursion1(0, 0, n)
    print(result)