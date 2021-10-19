from collections import deque

def bfs(v):
    q = deque([v])
    adj[v[0]][v[1]] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x = q.popleft()
        for a, b in zip(dx, dy):
            nx = x[0] + a
            ny = x[1] + b
            if (0<=nx<n and 0<=ny<m) and adj[nx][ny] == 1:
                adj[nx][ny] = 0
                q.append([nx, ny])
    return

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    adj = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        adj[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if adj[i][j] == 1:
                bfs([i, j])
                cnt += 1
    print(cnt)