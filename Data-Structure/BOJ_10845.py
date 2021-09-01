import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*N
begin, end = 0, 0

for _ in range(N):
    order, *val = input().split()
    if order == 'pop':
        if begin == end:
            print(-1)
        else:
            print(arr[begin])
            begin += 1
    elif order == 'front':
        if begin == end:
            print(-1)
        else:
            print(arr[begin])
    elif order == 'back':
        if begin == end:
            print(-1)
        else:
            print(arr[end-1])
    elif order == 'empty':
        if begin == end:
            print(1)
        else:
            print(0)
    elif order == 'size':
        print(end-begin)
    else:
        arr[end] = int(val[0])
        end += 1
