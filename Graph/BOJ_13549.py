from collections import deque

def bfs(start, end):
    q = deque()
    q.append(start)
    check = [False] * 200001
    visited = [0] * 200001
    while q:
        x = q.popleft()
        if x == end:
            return visited[x]
        if 0 <= x*2 < 200001 and not check[x*2]:
            q.appendleft(x*2)
            check[x*2] = True
            visited[x*2] = visited[x]
        if 0 <= x-1 < 200001 and not check[x-1]:
            q.append(x-1)
            check[x-1] = True
            visited[x-1] = visited[x] + 1
        if 0 <= x+1 < 200001 and not check[x+1]:
            q.append(x+1)
            check[x+1] = True
            visited[x+1] = visited[x] + 1

n, k = map(int, input().split())
print(bfs(n, k))