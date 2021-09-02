import sys
N, M = map(int, input().split())

edges = [] # 간선 리스트
ad_arr = [[False]*N for _ in range(N)] # 인접 행렬
ad_list = [[] for _ in range(N)] # 인접 리스트

for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a, b))
    edges.append((b, a))
    ad_arr[a][b] = ad_arr[b][a] = True
    ad_list[a].append(b)
    ad_list[b].append(a)

M *= 2
for i in range(M):
    for j in range(M):
        A, B = edges[i]
        C, D = edges[j]
        if A==B or A==C or A==D or B==C or B==D or C==D:
            continue
        if not ad_arr[B][C]:
            continue
        for edge in ad_list[D]:
            if A==edge or B==edge or C==edge or D==edge:
                continue
            print(1)
            sys.exit(0)
print(0)