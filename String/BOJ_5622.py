number = list(input())
cnt = 0
for n in number:
    if n in 'ABC':
        cnt += 3
        continue
    if n in 'DEF':
        cnt += 4
        continue
    if n in 'GHI':
        cnt += 5
        continue
    if n in 'JKL':
        cnt += 6
        continue
    if n in 'MNO':
        cnt += 7
        continue
    if n in 'PQRS':
        cnt += 8
        continue
    if n in 'TUV':
        cnt += 9
        continue
    if n in 'WXYZ':
        cnt += 10
print(cnt)