from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

# 경로가 있는지 탐색
def bfs(c):
    queue = deque([start_node])
    visited = [False] * (n+1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

start = 1000000000
end = 1

for _ in range(m):
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    start = min(start, weight) # 가장 중량이 작은 값
    end = max(end, weight) # 가장 중량이 큰 값

start_node, end_node = map(int, input().split())

result = start
while start <= end:
    mid = (start+end)//2
    if bfs(mid):
        result = mid
        start = mid+1
    else:
        end = mid-1
print(result)