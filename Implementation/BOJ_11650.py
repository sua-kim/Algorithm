N = int(input())
dot_list = [tuple(map(int, input().split())) for _ in range(N)]
dot_list.sort()
for idx in range(N):
    print(dot_list[idx][0], end=' ')
    print(dot_list[idx][1])