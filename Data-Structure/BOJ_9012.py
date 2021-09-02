N = int(input())
for _ in range(N):
    arr = list(input())
    stack = []
    is_empty = False
    for char in arr:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                is_empty = True
                break
            else:
                stack.pop()
    if not stack and not is_empty:
        print("YES")
    else:
        print("NO")