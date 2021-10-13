n = int(input())
i = 1
second = 0
while n > 0:
    if i > n:
        i = 1
    n -= i
    i += 1
    second += 1
print(second)