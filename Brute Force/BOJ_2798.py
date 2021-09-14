# 내 풀이(조합 사용)
'''
import itertools
N, M = map(int, input().split())
card_list = list(map(int, input().split()))
three_card = list(itertools.combinations(card_list, 3))
maximum = 0
for card in three_card:
    value = sum(card)
    if value > M:
        continue
    else:
        if value > maximum:
            maximum = value
        else:
            continue
print(maximum)
'''

# 다른 풀이(삼중 반복문 사용)
'''
N, M = map(int, input().split())
card_list = list(map(int, input().split()))
max = 0
three_card = list()
for i in range(len(card_list)):
    three_card.append(card_list[i])
    for j in range(i+1, len(card_list)):
        three_card.append(card_list[j])
        for k in range(j+1, len(card_list)):
            three_card.append(card_list[k])
            value = sum(three_card)
            if max < value <= M:
                max = value
            three_card.pop()
        three_card.pop()
    three_card.pop()
print(max)
'''

# 모범 풀이
N, M = map(int, input().split())
card_list = list(map(int, input().split()))
result = 0
length = len(card_list)
for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_value = card_list[i] + card_list[j] + card_list[k]
            if sum_value <= M:
                result = max(result, sum_value)
print(result)