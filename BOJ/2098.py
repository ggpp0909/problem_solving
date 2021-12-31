N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
dp = [[9999999 for i in range(1 << N)] for j in range(N)]

def recur(cur, visit, cnt):
    if cnt == N - 1:
        if arr[cur][0]:
            return arr[cur][0]
        return 9999999

    if dp[cur][visit] != 9999999:
        return dp[cur][visit]

    for i in range(N):
        bit = 1 << i
        if arr[cur][i] == 0 or visit & bit:
            continue
        dp[cur][visit] = min(dp[cur][visit], recur(i, visit | bit, cnt + 1) + arr[cur][i])

    return dp[cur][visit]

print(recur(0, 1, 0))