from collections import Counter
a = Counter(list(input().upper()))
res = list(a.most_common())
max_num = res[0][1]
if len(res) > 1 and res[1][1] == max_num:
    print('?')
else:
    print(res[0][0])