import sys
input = sys.stdin.readline

def recursion(N, M, position, result):
    if position >= N:
        for i in result:
            print(i, end=' ')
        print()
        position = 0
        result = [0] * M
    for i in range(1, N + 1):
        if i not in result:
            result[position] = i
            position += 1
        recursion(N, M, position, result)

N, M = map(int, input().split())
recursion(N, M, 0, [0]*M)


