# 이전 순열이 있는지 알려주는 함수
def prev_permutation(a):
    i = len(a) - 1
    # i 찾기: 오름차순이 깨지는 순간의 인덱스 i 검색
    while i > 0 and a[i-1]<a[i]:
        i -= 1
    # 이전 순열이 없는 경우 False 리턴
    if i == 0:
        return False
    # j 찾기: a[i-1]과 교환할 수 찾기
    j = len(a) - 1
    while a[i-1] <= a[j]:
        j -= 1
    # swap
    a[i-1], a[j] = a[j], a[i-1]
    # i부터 내림차순 정렬
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
a = list(map(int, input().split()))
if prev_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)

