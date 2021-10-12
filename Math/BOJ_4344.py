c = int(input())
for _ in range(c):
    n, *arr = map(int, input().split())
    avg = sum(arr)/n
    cnt = 0
    for a in arr:
        if a > avg:
           cnt += 1
    print('{0:0.3f}%'.format(cnt/n*100))