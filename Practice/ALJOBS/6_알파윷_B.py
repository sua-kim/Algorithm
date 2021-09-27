N = int(input())
move_list = list(map(int, input().split()))

score = [0, 5, 10, 15, 20, 50, 30, 35, 40, 45, 100, 55, 60, 65, 70, 75, 80, 85, 90, 95, 500, 1000]
position = 0
for move in move_list:
    position += move
    if position >= len(score)-1:
        print(1000)
        break
    print(score[position], end=' ')