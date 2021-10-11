max_value = 0
index = 0
for i in range(1, 10):
    n = int(input())
    if max_value < n:
        max_value = n
        index = i
print(max_value)
print(index)