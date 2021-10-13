n = int(input())
n_list = [int(input()) for _ in range(n)]
left, right = 1, 1
max_left, max_right = n_list[0], n_list[-1]
for i in range(1, len(n_list)):
    if max_left < n_list[i]:
        max_left = n_list[i]
        left += 1

for i in range(len(n_list)-2, -1, -1):
    if n_list[i] > max_right:
        max_right = n_list[i]
        right += 1

print(left)
print(right)