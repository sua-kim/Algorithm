from sys import stdin
input = stdin.readline

N = int(input())
stack = []
for _ in range(N):
    order, *arr = input().split()
    if order == 'push':
        stack.append(arr[0])
    elif order == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        print(1 if not stack else 0)
    else:
        print(-1 if not stack else stack[-1])