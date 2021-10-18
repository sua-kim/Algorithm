import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1) # 연결된 간선의 개수
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

heap = []

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    x = heapq.heappop(heap)
    result.append(x)
    for y in graph[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            heapq.heappush(heap, y)

print(' '.join(map(str, result)))