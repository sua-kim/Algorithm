def solve(n, x, y):
    global result
    if n == 2:
        if x == r and y == c:
            print(result)
            return
        result += 1
        if x == r and y+1 == c:
            print(result)
            return
        result += 1
        if x+1 == r and y == c:
            print(result)
            return
        result += 1
        if x+1 == r and y+1 == c:
            print(result)
            return
        result += 1
        return
    solve(n/2, x, y)
    solve(n/2, x, y+n/2)
    solve(n/2, x+n/2, y)
    solve(n/2, x+n/2, y+n/2)

result = 0
N, r, c = map(int, input().split())
solve(2**N, 0, 0)