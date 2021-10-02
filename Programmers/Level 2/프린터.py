from collections import deque

def solution(priorities, location):
    answer = 0
    p = deque()
    p += enumerate(priorities, start=0)
    priorities.sort()
    while len(p) > 0:
        if p[0][1] == priorities[-1]:
            answer += 1
            if p[0][0] == location:
                break
            p.popleft()
            priorities.pop()
            continue
        x = p.popleft()
        p.append(x)
    return answer

print(solution([1, 1, 9, 1, 1, 1,], 0))
