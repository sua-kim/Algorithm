def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
        return answer
    number = list(map(str, [i for i in range(10)]))
    for i in range(len(s)):
        if s[i] not in number:
            answer = False
            break
    return answer

def solution1(s):
    answer = False
    if s.isdigit() and len(s) in [4, 6]:
        answer = True
    return answer