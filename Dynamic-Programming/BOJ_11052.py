N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0] * 1001
dp[1] = P[1]

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[1]
    if P[i] > dp[i]:
        dp[i] = P[i]

print(dp[0:5])
print(dp[N])