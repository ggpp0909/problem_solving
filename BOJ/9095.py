n = int(input())
dp = [0 for i in range(20)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 20):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(n):
    m = int(input())
    print(dp[m])