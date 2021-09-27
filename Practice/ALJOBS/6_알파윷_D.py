N = int(input())
move_list = list(map(int, input().split()))
order = list(map(int, input().split()))

# 4개 말에 대한 위치 리스트
result = [0] * 4

# 위치
position = 0

# 점수의 총 합
score_sum = [0] * 4

# 이동 알고리즘
score = [0, 5, 10, 15, 20, 50, 30, 35, 40, 45, 100, 55, 60, 65, 70, 75, 80, 85, 90, 95, 500, 1000,
         275, 250, 300, 150, 175, 150, 125, 350, 400]

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

for i in range(N):
    # 어떤 말이 움직였는가
    person = order[i] -1
    move = move_list[i]
    position = result[person]  # 그 사람의 position

    # 그 말에 대한 position을 저장
    if position in moving.keys():
        position = moving[position][move-1]
    else:
        position += move
        if position >= 21:
            score_sum[person] = 1000
    if position == 21:
        score_sum[person] += 1000
        continue

    # 말의 위치가 겹치는 경우
    if position in result:
        print(-1)
        exit(0)
    result[person] = position
    score_sum[person] = score[position]

print(sum(score_sum))
