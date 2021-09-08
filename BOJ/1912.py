import sys

n = int(input())
arr = [-10000] + list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0 for i in range(n + 1)]

for i in range(n + 1):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])

print(max(dp))