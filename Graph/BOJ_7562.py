from collections import deque

def bfs(n, start, end):
    q = deque()
    q.append(start)
    visited = [[0]*n for _ in range(n)]
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, -2, -1, 1, 2]
    while q:
        x = q.popleft()
        if x[0] == end[0] and x[1] == end[1]:
            return visited[x[0]][x[1]]
        for a, b in zip(dx, dy):
            nx, ny = x[0]+a, x[1]+b
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x[0]][x[1]] + 1

t = int(input())
for _ in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    result = bfs(n, start, end)
    print(result)