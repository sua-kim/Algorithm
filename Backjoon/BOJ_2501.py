# 제출 답안
def kth_divisor(N, K):
    divisor = []
    for i in range(N):
        if (N % (i+1) == 0):
            divisor.append(i+1)
    if K > len(divisor):
        return 0
    else:
        return divisor[K-1]

N, K = map(int, input().split())
print(kth_divisor(N, K))

# 수정 답안 : pythonic code 적용
N, K = map(int, input().split())
divisor = [n+1 for n in range(N) if N%(n+1) == 0]
print(divisor)
if len(divisor) < K: print(0)
else: print(divisor[K-1])
