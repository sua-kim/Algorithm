'''
예제) 약수의 개수가 홀수인 수
1부터 N까지의 숫자들 중에서 약수의 개수가 홀수인 숫자들의 개수를 출력하는 프로그램을 작성하여라
'''

N = int(input())
'''
i = 1
count = 0
while i <= N:
    if N >= i**2:
        count += 1
    i += 1

print(count)
'''

result = 0

for i in range(1, N+1):
    count = 0
    for j in range(1, i+1):
        if i%j==0:
            count += 1
    if count % 2 == 1:
        result += 1

print(result)