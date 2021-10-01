from collections import deque
# n: 정점의 개수, m: 간선의 개수, v: 시작점
n, m, v = map(int, input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
    k, l = map(int, input().split())
    a[k].append(l)
    a[l].append(k)
for i in range(1, n+1):
    a[i].sort()

'''
DFS: 깊이 우선 탐색
갈 수 있는 끝까지 갔다가 다시 돌아오는 형식 -> 재귀호출로 구현
= 방문했다는 표시로 재귀함수 호출
'''
# check 배열 : 방문했는지 확인하는 배열
check = [False] * (n+1)
def dfs(x):
    global check
    # 방문 체크
    check[x] = True
    print(x, end = ' ')
    # 인접리스트에 있는 모든 노드 방문
    for vertex in a[x]:
        # 이미 이전에 방문한 노드가 아니라면
        if not check[vertex]:
            dfs(vertex)

'''
BFS: 너비 우선 탐색
한 노드에서 갈 수 있는 모든 노드를 고려 -> 큐로 구현
= 방문했다는 표시로 큐 삽입
'''
def bfs(start):
    # 방문했는지 확인하는 배열 check(지역변수)
    check = [False] * (n+1)
    q = deque()
    q.append(start)
    check[start] = True
    # 큐가 빌 때까지 노드 방문 계속 방문
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for vertex in a[x]:
            if not check[vertex]:
                check[vertex] = True
                q.append(vertex)

dfs(v)
print()
bfs(v)
