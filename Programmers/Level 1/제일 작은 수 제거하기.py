def solution(arr):
    min_value = min(arr)
    arr.remove(min_value)
    if arr:
        answer = arr
    else:
        answer = [-1]
    return answer