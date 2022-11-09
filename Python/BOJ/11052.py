n = int(input())

arr = list(map(int, input().split()))
dp = [0 for i in range(n + 1)]
dp[0] = arr[0]

for i in range(1, n):
    for j in range(i + 1):
        dp[i] = max(dp[i], dp[i-j-1] + arr[j])

print(dp[n - 1])
