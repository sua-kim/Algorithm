d, n = map(int, input().split())
d_list = list(map(int, input().split()))
n_list = list(map(int, input().split()))

# 이분탐색을 위한 변경
for i in range(1, len(d_list)):
    if d_list[i-1] < d_list[i]:
        d_list[i] = d_list[i-1]

position = 0 # 도우가 쌓이는 위치
start, end = 0, len(d_list)-1
for dough in n_list:
    possible = False
    while start <= end:
        mid = (start+end) // 2
        if d_list[mid] >= dough:
            start = mid + 1
            position = mid
            possible = True
        else:
            end = mid - 1
    if not possible:
        position = -1
        break

    start = 0
    end = position - 1

if position == -1:
    print(0)
else:
    print(position + 1)