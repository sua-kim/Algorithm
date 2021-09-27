def solution(x):
    number = map(int, list(str(x)))
    if x % sum(number) == 0:
        answer = True
    else:
        answer = False
    return answer