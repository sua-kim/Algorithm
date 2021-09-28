# collections.Counter 객체 이용하기
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 해시 함수 이용하기
def solution2(participant, completion):
    temp = 0
    dic = dict()
    for part in participant:
        dic[hash(part)] = part
        temp += hash(part)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer