def solution(n):
    answer = 0
    x = 1
    issquared = False
    while True:
        if n == x**2:
            issquared = True
        if n < x**2:
            break
        x += 1
    if issquared:
        answer = x**2
    else:
        answer = -1
    return answer

def solution1(n):
    sqrt = n**(1/2)
    if sqrt % 1 == 0:
        return (sqrt+1)**2
    return -1