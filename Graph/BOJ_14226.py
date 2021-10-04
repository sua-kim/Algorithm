from collections import deque

def bfs(s):
    q = deque()
    q.append((1, 0))
    time = [[-1] * (s+1) for _ in range(s+1)]
    time[1][0] = 0
    while q:
        x, y = q.popleft()
        if x == s:
            return time[x][y]
        if time[x][x] == -1:
            time[x][x] = time[x][y] + 1
            q.append((x, x))
        if x+y <= s and time[x+y][y] == -1:
            time[x+y][y] = time[x][y] + 1
            q.append((x+y, y))
        if x-1 >= 0 and time[x-1][y] == -1:
            time[x-1][y] = time[x][y] + 1
            q.append((x-1, y))


s = int(input())
print(bfs(s))