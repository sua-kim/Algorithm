'''
BOJ_17427 - 약수의 합 2
'''

# 시간 초과 발생
'''
N = int(input())
sum = 0
for i in range(1, N+1):
    for j in range(1, int(i**(1/2))+1):
        if i % j == 0:
            sum += j
            if j != i**(1/2):
                sum += i//j
print(sum)
'''

# 해결 - 배수의 개념으로 접근
N = int(input())
sum = 0
for i in range(1, N+1):
    sum += i * (N//i)
print(sum)
