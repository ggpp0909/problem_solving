n, k = map(int, input().split())
arr = [int(input()) for i in range(n)]
inf = 9999999999
dp = [inf for i in range(k + 1)]
dp[0] = 0
for coin in arr:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i - coin] + 1, dp[i])

if dp[-1] == inf:
    print(-1)
else:
    print(dp[-1])
