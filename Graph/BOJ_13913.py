from collections import deque

def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [0] * 200001
    path = [0 for _ in range(100001)]
    path[start] = start
    while q:
        x = q.popleft()
        if x == end:
            return visited[x], path
        for nx in [x-1, x+1, x*2]:
            if 0 <= nx < 100001 and visited[nx] == 0:
                q.append(nx)
                path[nx] = x
                visited[nx] = visited[x] + 1

start, end = map(int, input().split())
res1, res2 = bfs(start, end)
print(res1)
arr = [end]
temp = end
for _ in range(res1):
    arr.append(res2[temp])
    temp = res2[temp]
print(' '.join(map(str, arr[::-1])))