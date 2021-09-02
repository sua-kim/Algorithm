import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 20000
begin, end = 10000, 10000

for _ in range(N):
    order, *value = input().split()
    if order == 'push_front':
        begin -= 1
        arr[begin] = value[0]
    elif order == 'push_back':
        arr[end] = value[0]
        end += 1
    elif order == 'pop_front':
        if begin == end:
            print(-1)
        else:
            print(arr[begin])
            begin += 1
    elif order == 'pop_back':
        if begin == end:
            print(-1)
        else:
            print(arr[end-1])
            end -= 1
    elif order == 'size':
        if begin == end:
            print(0)
        else:
            print(end-begin)
    elif order == 'empty':
        if begin == end:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if begin == end:
            print(-1)
        else:
            print(arr[begin])
    else:
        if begin == end:
            print(-1)
        else:
            print(arr[end-1])
