import heapq

n = int(input())
card_list = [int(input()) for _ in range(n)]
heapq.heapify(card_list)
result = 0
while len(card_list) != 1:
    a = heapq.heappop(card_list)
    b = heapq.heappop(card_list)
    result += (a+b)
    heapq.heappush(card_list, a + b)

print(result)