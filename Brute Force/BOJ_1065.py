n = int(input())
cnt = 0

def isNum(n):
    res = True
    if n < 10:
        return res
    n_list = list(map(int, list(str(n))))
    temp = n_list[1] - n_list[0]
    if len(n_list) >= 3 and temp != n_list[2]-n_list[1]:
        res = False
    return res

for i in range(1, n+1):
    if isNum(i):
        cnt +=1

print(cnt)
