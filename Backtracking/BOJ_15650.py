N, M = map(int, input().split())
'''
# 순서가 있는 경우로 푼 예시

a = [0] * M

def recursion(index, start, N, M):
    if index == M:
        print(' '.join(map(str, a)))
        return
    for i in range(start, N+1):
        a[index] = i
        recursion(index+1, i+1, N, M)

recursion(0, 1, N, M)
'''

# 선택인 경우로 푼 예시
count = 0
a = [0] * M
def recursion(index, count, N, M):
    if count == M:
        print(' '.join(map(str, a)))
        return
    # N개를 못 골랐는데 끝난 경우
    if (index > N):
        return
    # 선택을 한 경우
    a[count] = index
    recursion(index+1, count+1, N, M)
    # 선택을 하지 않은 경우
    a[count] = 0
    recursion(index + 1, count, N, M)

recursion(1, 0, N, M)