from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

def bfs(x):
    global checked
    q = deque([x])
    checked[x] = 1
    while q:
        k = q.popleft()
        for vertex in graph[k]:
            if checked[vertex] == checked[k]:
                return False
            if checked[vertex] == 0:
                checked[vertex] = -checked[k]
                q.append(vertex)
    return True

for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    checked = [0] * (v+1)
    res = 0
    for node in range(1, v+1):
        if checked[node] == 0:
            if not bfs(node):
                res = -1
                break
    print('YES' if res == 0 else 'NO')
