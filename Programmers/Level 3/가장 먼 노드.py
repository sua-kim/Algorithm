import collections


def bfs(n, graph):
    visited = [False] * (n + 1)
    dist = [-1] * (n + 1)
    q = collections.deque([1])
    visited[1] = True
    dist[1] = 0
    while q:
        x = q.popleft()
        for node in graph[x]:
            if not visited[node]:
                visited[node] = True
                dist[node] = dist[x] + 1
                q.append(node)
    return dist


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for node1, node2 in edge:
        graph[node1].append(node2)
        graph[node2].append(node1)
    distance = bfs(n, graph)
    maximum = max(distance)
    for k in distance:
        if k == maximum:
            answer += 1
    return answer