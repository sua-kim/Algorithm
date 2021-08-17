'''
BOJ_15552 : 빠른 A+B
'''

from sys import stdin
input = stdin.readline

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    print(a+b)