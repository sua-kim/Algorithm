import re

def solution(dartResult):
    answer = 0
    exp = []
    c = 0
    dartArr = re.split('([SDT]|[r*#])', dartResult)
    dartArr = list(filter(lambda x: x != '', dartArr))
    for i in dartArr:
        if i not in ['S', 'D', 'T', '*', '#']:
            exp.append(int(i))
        elif i == 'D':
            exp[-1] **= 2
        elif i == 'T':
            exp[-1] **= 3
        elif i == '*':
            exp[-1] *= 2
            if len(exp) >=2:
                exp[-2] *= 2
        elif i == '#':
            exp[-1] *= (-1)
        else:
            continue
    answer = sum(exp)
    return answer
