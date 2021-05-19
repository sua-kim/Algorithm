def solution(nums):
    answer = 0
    type = []
    for i in nums:
        if len(type) >= len(nums)/2:
            break;
        if i not in type:
            type.append(i)
    answer = len(type)
    return answer
