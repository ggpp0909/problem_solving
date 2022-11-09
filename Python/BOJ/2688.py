dp = [[0 for i in range(10)] for j in range(65)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, 65):
    for j in range(10):
        tot = 0
        for k in range(0, j + 1):
            tot += dp[i-1][k]
        dp[i][j] = tot

tc = int(input())
for _ in range(tc):
    n = int(input())

    ans = 0
    for i in range(10):
        ans += dp[n][i]

    print(ans)


