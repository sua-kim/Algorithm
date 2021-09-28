# 다음 순열이 있는지 없는지 알려주는 함수
def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0: # 마지막 순열일 경우
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1

    # swap
    a[i-1], a[j] = a[j], a[i-1]

    # 마지막 순열 뒤집기
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

n = int(input())
a = list(map(int, input().split()))
if next_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)