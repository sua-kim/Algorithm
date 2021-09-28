def solution(s):
    answer = True
    s = s.lower()
    p, y = 0, 0
    for str in s:
        if str == 'p':
            p += 1
        if str == 'y':
            y += 1
    if p-y != 0:
        answer = False
    return answer

def solution1(s):
    return s.lower().count('p') == s.lower().count('y')