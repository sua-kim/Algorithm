n = int(input())

# 브루트포스
'''
count = 0
def recursion(n, index, one, two):
    if one + 2*two == n:
        global count
        count += 1
        return
    if index >= n:
        return
    recursion(n, index+1, one+1, two)
    recursion(n, index+1, one, two+1)

recursion(n, 0, 0, 0)
print(count%10007)
'''

# DP
'''
D = [0] * 1001
D[1] = 1
D[2] = 2
for i in range(3, n+1):
    D[i] = D[i-1] + D[i-2]
print(D[n]%10007)
'''

dp = [0 for _ in range(n+1)]

if n <= 3: print(n)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[i]%10007)