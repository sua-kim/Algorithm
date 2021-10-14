def solution(brown, yellow):
    answer = []
    for i in range(yellow, 0, -1):
        if yellow % i == 0 and (i*2+yellow//i*2+4 == brown):
            answer = [i+2, yellow//i+2]
            break
    return answer