from collections import deque

def bfs(graph, i, j, n):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()
    q.append((i, j))
    checked[i][j] = True
    count = 1
    while q:
        position = q.popleft()
        for a, b in zip(dx, dy):
            x, y = position[0]+a, position[1]+b
            if x < 0 or x >= n: continue
            if y < 0 or y >= n: continue
            if graph[x][y] == 1 and not checked[x][y]:
                q.append((x, y))
                checked[x][y] = True
                count += 1
    return count

n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]
checked = [[False]*n for _ in range(n)]
number = 0
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not checked[i][j]:
            temp = bfs(graph, i, j, n)
            result.append(temp)
            number += 1

print(number)
for res in sorted(result):
    print(res)