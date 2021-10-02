from collections import deque
def solution(progresses, speeds):
    answer = []
    p = deque(progresses)
    s = deque(speeds)
    while p:
        count = 0
        day = (100-p[0])//s[0]
        if (100-p[0])%s[0] != 0:
            day += 1
        for i in range(len(p)):
            p[i] += day*s[i]
        while p and p[0] >= 100:
            p.popleft()
            s.popleft()
            count += 1
        answer.append(count)
    return answer