def solution(n):
    n = map(int, list(str(n)))
    n = sorted(n, reverse=True)
    answer = int(''.join(map(str, n)))
    return answer