from collections import deque

def bfs(m, n, tomato, visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    riped = tomato
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                q.append((i, j))
                visited[i][j] = True
    temp = -1
    if len(q) == m*n:
        return 0
    while q:
        x_list = []
        temp += 1
        for _ in range(len(q)):
            x_list.append(q.popleft())
        for x in x_list:
            for a, b in zip(dx, dy):
                nx, ny = x[0] + a, x[1] + b
                if 0 <= nx < n and 0 <= ny < m:
                    if tomato[nx][ny] == 0 and not visited[nx][ny]:
                        q.append((nx, ny))
                        riped[nx][ny] = 1
                        visited[nx][ny] = True
    for i in range(n):
        if 0 in riped[i]:
            temp = -1
            break
    return temp

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
print(bfs(m, n, tomato, visited))

