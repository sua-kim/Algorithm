s_list = list(input())
result = []
temp = ord('a')
while temp <= 122:
    if chr(temp) in s_list:
        result.append(s_list.index(chr(temp)))
    else:
        result.append(-1)
    temp += 1

print(' '.join(map(str, result)))