from collections import deque

n = int(input())
edge = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(edge):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        for node in adj[x]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
    return

bfs(1)
print(visited.count(True)-1)