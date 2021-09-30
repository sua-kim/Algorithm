L, C = map(int, input().split())
C_list = input().split()
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
def check(password):
    ja = 0
    mo = 0
    for x in password:
        if x in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


# 모범 답안
def go(L, C_list, password, index):
    if len(password) == L:
        # 최소 한개의 모음
        if check(password):
            print(password)
        return
    if index == len(C_list):
        return
    # index를 사용하는 경우와 사용하지 않는 경우
    go(L, C_list, password+C_list[index], index+1)  #
    go(L, C_list, password, index+1)