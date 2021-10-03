def solution(n):
    answer = 0
    div_list = [1] * (n+1)
    for i in range(2, n+1):
        k = 1
        while i*k <= n:
            div_list[i*k] += 1
            k += 1
    for j in range(2, n+1):
        if div_list[j] == 2:
            answer += 1
    return answer