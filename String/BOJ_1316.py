t = int(input())
cnt = 0
for _ in range(t):
    word = input()
    repeat = []
    for i in word:
        if not repeat:
            repeat.append(i)
        if repeat[-1] != i:
            repeat.append(i)
    if len(repeat) == len(set(word)):
        cnt += 1
print(cnt)