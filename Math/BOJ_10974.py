# 다음 순열이 있는지 구하는 함수
def next_permutation(a):
    i = len(a) - 1
    # i 찾기: 내림차순이 안되는 순간(마지막 순열 찾기)
    while i > 0 and a[i-1] > a[i]:
        i -= 1
    # 다음 순열이 없다면 False 리턴
    if i == 0:
        return False
    # a[i-1]과 swap할 j 찾기
    j = len(a) - 1
    while a[i-1] >= a[j]:
        j -= 1
    # swap
    a[i-1], a[j] = a[j], a[i-1]
    # i 이후 수 오름차순으로 변경
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

N = int(input())
N_list = [i for i in range(1, N+1)]
print(' '.join(map(str,N_list)))
while next_permutation(N_list):
    print(' '.join(map(str, N_list)))