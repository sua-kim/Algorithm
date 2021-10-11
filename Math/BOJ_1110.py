n = input()
if len(n) == 1:
    n = '0' + n
a, b = list(map(int, list(n)))
c, d = a, b
count = 0
while True:
    temp = c
    c = d
    d = (temp+d)%10
    count += 1
    if c == a and d == b:
        break
print(count)