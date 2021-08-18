'''
BOJ_2729 - 이진수 덧셈
'''

N = int(input())

for i in range(N):
    a, b = map(lambda x: int(x, base=2), input().split())
    print(bin(a+b)[2:])