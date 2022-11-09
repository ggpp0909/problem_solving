n, k = map(int, input().split())
coin = [int(input()) for i in range(n)]
coin.sort()

dp = [0 for i in range(k + 1)]

for i in range(n):
    for j in range(i, k + 1):
        if j == coin[i]:
            dp[j] += 1
        elif j > coin[i]:
            dp[j] += dp[j - coin[i]]

print(dp[k])