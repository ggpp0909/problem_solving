T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(2)]
    dp = [[0 for i in range(N + 1)] for j in range(2)]

    dp[0][1] = arr[0][0]
    dp[1][1] = arr[1][0]

    for i in range(2, N + 1):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + arr[0][i - 1]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i - 1]
    
    print(max(dp[0][-1], dp[1][-1]))

