from collections import deque

def bfs(maze, visited, n, m):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((0, 0))
    dist = [[0] * m for _ in range(n)]
    visited[0][0] = True
    dist[0][0] = 1
    while q:
        x = q.popleft()
        for a, b in zip(dx, dy):
            nx, ny = x[0]+a, x[1]+b
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x[0]][x[1]] + 1
                    visited[nx][ny] = True
    return dist

n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
res = bfs(maze, visited, n, m)
print(res[n-1][m-1])