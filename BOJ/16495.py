n, k = map(int, input().split())

dp = [[0] * (n + 10) for i in range(n + 10)]


for i in range(n + 10):
    dp[i][0] = 1
    dp[i][i] = 1

for i in range(1, n + 10):
    for j in range(1, n + 10):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

print(dp[n - 1][k - 1])