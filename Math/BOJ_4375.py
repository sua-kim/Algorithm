'''
BOJ_4375 - 1
'''

# 내가 짠 코드
'''
n = int(input())
i, count = 0, 0
try:
    while 1:
       count += ((10**i)%n)
       i += 1
       if (count % n == 0):
           print(i)
           n = int(input())
           i, count = 0, 0
except:
    exit()
'''

# 모범 코드
while True:
    try:
        n = int(input())
    except:
        break
    num = 0
    i = 1
    while True:
        num = num * 10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1