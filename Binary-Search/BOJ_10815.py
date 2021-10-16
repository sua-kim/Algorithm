n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

result = []
for card in m_list:
    start = 0
    end = n-1
    temp = False
    while start <= end:
        mid = (start+end)//2
        if n_list[mid] == card:
            temp = True
            break
        if n_list[mid] > card:
            end = mid - 1
        else:
            start = mid + 1
    if temp:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))