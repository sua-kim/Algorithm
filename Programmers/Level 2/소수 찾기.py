from itertools import permutations
def solution(numbers):
    answer = 0
    num = []
    for i in range(1, len(numbers)+1):
        for s in permutations(numbers, i):
            num.append(''.join(s))
    num = list(set(map(int, num)))
    for n in num:
        temp = True
        if n in [0, 1]:
            continue
        for i in range(2, n):
            if n % i == 0:
                temp = False
                break
        if temp:
            answer += 1
    return answer