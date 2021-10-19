from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    visited[start] = True
    cnt = 1
    while q:
        x = q.popleft()
        for node in adj[x]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
                cnt += 1
    return cnt

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[b].append(a)
max_num = 0
result = []
for i in range(1, n+1):
    visited = [False] * (n + 1)
    if adj[i]:
        temp = bfs(i)
        max_num = max(max_num, temp)
        result.append((i, temp))
for i in result:
    if i[1] == max_num:
        print(i[0], end=' ')