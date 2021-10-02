# 내 풀이
def solution(citations):
    answer = 0
    count = 0
    find = False
    citations.sort()
    for i in range(len(citations)-1, -1, -1):
        count += 1
        if count == citations[i]:
            find = True
            answer = citations[i]
        if count > citations[i]:
            if answer == citations[i]:
                answer = 0
            if (not find) and (answer != citations[i]):
                answer = count-1
            return answer
    answer = len(citations)
    return answer

# 다른 사람의 풀이
def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
