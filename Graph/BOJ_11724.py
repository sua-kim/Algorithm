from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

# 노드 방문여부를 저장하는 변수
check = [False] * (n + 1)

# 너비우선탐색: 한 노드에서 갈 수 있는 노드를 모두 저장 -> 방문의 표시로 큐 삽입
def bfs(start):
    global check
    q = deque([start])
    check[start] = True
    while q:
        x = q.popleft()
        for vertex in a[x]:
            if not check[vertex]:
                q.append(vertex)
                check[vertex] = True

# 연결요소 개수 저장하는 변수 선언
count = 0

for i in range(1, n + 1):
    if not check[i]:
        bfs(i)
        count += 1
print(count)
