H, M = map(int, input().split())
if M < 45:
    M += (60 - 45)
    H -= 1
else:
    M -= 45
if H < 0:
    H += 24
print(H, M)