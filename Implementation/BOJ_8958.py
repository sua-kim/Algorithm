t = int(input())
for _ in range(t):
    quiz_list = list(input())
    temp, score = 0, 0
    for quiz in quiz_list:
        if quiz == 'X':
            temp = 0
            continue
        temp += 1
        score += temp
    print(score)
