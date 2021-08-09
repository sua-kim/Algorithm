N = int(input())
score = list(map(int, input().split()))

avg = round(sum(score)/N)
minus = []

for i in score:
    minus.append(abs(i-avg))

print('{0} {1}'.format(avg, minus.index(min(minus))))
