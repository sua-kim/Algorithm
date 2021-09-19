N = int(input())
k = 1
second = 0

while N > 0:
    if N < k:
        k = 1
    N -= k
    k += 1
    second += 1

print(second)