N = int(input())
move_list = list(map(int, input().split()))

score = [0, 5, 10, 15, 20, 50, 30, 35, 40, 45, 100, 55, 60, 65, 70, 75, 80, 85, 90, 95, 500, 1000,
         275, 250, 300, 150, 175, 150, 125, 350, 400]
# 두둔
moving = {
    5: [22, 23, 24, 25, 26],
    10: [27, 28, 24, 29, 30],
    22: [23, 24, 25, 26, 15],
    23: [24, 25, 26, 15, 16],
    24: [29, 30, 20, 21, 21],
    25: [26, 15, 16, 17, 18],
    26: [15, 16, 17, 18, 19],
    27: [28, 24, 29, 30, 20],
    28: [24, 29, 30, 20, 21],
    29: [30, 20, 21, 21, 21],
    30: [20, 21, 21, 21, 21]
}
position = 0

for move in move_list:
    # 더해도 되는지 먼저 판단 필요
    if position in moving.keys():
        position = moving[position][move-1]
    else:
        position += move
        if position >= 21:
            print(1000)
            break
    if position == 21:
        print(1000)
        break
    print(score[position], end=' ')