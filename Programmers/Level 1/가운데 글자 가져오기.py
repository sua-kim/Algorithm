def solution(s):
    answer = ''
    k = len(s) // 2
    answer = s[k-1:k+1] if len(s) % 2 == 0 else s[k]
    return answer