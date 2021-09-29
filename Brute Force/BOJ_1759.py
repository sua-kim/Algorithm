L, C = map(int, input().split())
C_list = list(input().split())
C_list.sort()
'''
arr = [''] * L
count = [0] * 2
def recursion(index, start, L, C, a, b):
    if index >= L:
        if a >= 1 and b >= 2:
            print(''.join(arr))
        return
    for i in range(start, C):
        if C_list[i] in ['a', 'e', 'i', 'o', 'u']:
            a_plus, b_plus = 1, 0
        else:
            a_plus, b_plus = 0, 1
        arr[index] = C_list[i]
        recursion(index+1, i+1, L, C, a+a_plus, b+b_plus)
        arr[index] = ''

recursion(0, 0, L, C, 0, 0)
'''

# 모범 답안
def go(index, count, N):
    if count == N:
        return
    if index >= N:
        return
