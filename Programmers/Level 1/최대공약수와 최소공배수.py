def solution(n, m):
    answer = []
    gcd, lcm = 0, 0
    a, b = n, m
    while b != 0:
        a, b = b, a%b
    gcd = a
    lcm = n*m/gcd
    answer = [gcd, lcm]
    return answer