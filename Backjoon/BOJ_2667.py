import sys
input = sys.stdin.readline

N = int(input())

graph = [list(input().rstrip()) for i in range(N)] 
visited = [[0] * N for i in range(N)]
houses = []
house = 0


def search(i, j): 
    global house

    if i < 0 or j >= N or i >= N or j < 0 or graph[i][j] == '0':
        return
    graph[i][j] = '0' 
    visited[i][j] = 1 
    house += 1  

    search(i + 1, j)
    search(i, j + 1)
    search(i - 1, j)
    search(i, j - 1)

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and graph[i][j] == '1':
            search(i,j)
            houses.append(house)
            house = 0

print(len(houses))
for i in sorted(houses):
    print(i)
