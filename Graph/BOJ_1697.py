from collections import deque

def bfs(start, end):
    q = deque()
    q.append(start)
    dx = [-1, 1, 2]
    visited = [0]*100001
    while q:
        x = q.popleft()
        if x == end:
            return visited[x]
        for a in dx:
            if a == 2:
                nx = x*2
            else:
                nx = x + a
            if 0<=nx<100001 and visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[x] + 1

start, end = map(int, input().split())
print(bfs(start, end))