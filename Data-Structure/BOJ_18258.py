import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    order, *arr = input().split()
    if order == 'push':
        queue.append(arr[0])
    elif order == 'pop':
        if queue:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        print(0 if queue else 1)
    elif order == 'front':
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)
