def solution(lottos, win_nums):
    score = [0, 6, 5, 4, 3, 2]
    number, cnt = 0, 0
    max_rank, min_rank = 0, 0
    for i in range(6):
        if lottos[i] == 0:
            cnt += 1
            continue
        if lottos[i] in win_nums:
            number += 1
    for rank in range(1, 6):
        if cnt + number == score[rank]:
            max_rank = rank
        if number == score[rank]:
            min_rank = rank
    if not min_rank:
        min_rank = 6
    if not max_rank:
        max_rank = 6
    answer = [max_rank, min_rank]
    return answer

k = solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
print(k)