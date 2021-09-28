# 다음 순열이 있는지 없는지 알려주는 함수
def next_permutation(a):
    i = len(a) - 1
    # i 찾기: 다음 순열 검색을 위해 오름차순 검색
    while i > 0 and a[i-1]>a[i]:
        i -= 1
    # 다음 순열이 없는 경우
    if i == 0:
        return False
    # j 찾기: a[i-1]과 swap할 원소 검색
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    # swap
    a[i-1], a[j] = a[j], a[i-1]
    # i번째 원소부터 오름차순 정렬
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
a = list(map(int, input().split()))
if next_permutation(a):
    print(" ".join(map(str, a)))
else:
    print(-1)