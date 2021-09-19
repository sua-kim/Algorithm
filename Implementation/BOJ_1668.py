N = int(input())
height_list = list()
left, right = 0, 0
left_count, right_count = 0, 0

for _ in range(N):
    height = int(input())
    height_list.append(height)
    if left < height:
        left = height
        left_count += 1

for i in range(N-1,-1,-1):
    if right < height_list[i]:
        right = height_list[i]
        right_count += 1

print(left_count)
print(right_count)