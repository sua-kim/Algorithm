n, c = map(int, input().split())
n_list = [int(input()) for _ in range(n)]
n_list.sort()
start = 1
end = n_list[-1] - n_list[0]

while start <= end:
    mid = (start + end) // 2  # mid는 Gap을 의미
    value = n_list[0]
    count = 1
    for i in range(1, len(n_list)):
        if n_list[i] >= value + mid:
            value = n_list[i]
            count += 1
    if count >= c:  # c개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1
        result = mid
    else:  # c개 이상의 공유기를 설치할 수 없는 경우
        end = mid - 1

print(result)