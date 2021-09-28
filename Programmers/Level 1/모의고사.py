def solution(answers):
    answer = []
    record = [0] * 4
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    i = 0
    for ans in answers:
        if ans == a[i % 5]:
            record[1] += 1
        if ans == b[i % 8]:
            record[2] += 1
        if ans == c[i % 10]:
            record[3] += 1
        i += 1
    max_score = max(record)
    answer = [i for i in range(4) if record[i] == max_score]
    return answer