N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
# visited = [False for i in range(N)]
dp = [[9999999 for i in range(1 << N)] for j in range(30)]


def recur(cur, visit):

    # if cur == N:
    if visit == (1 << N) - 1: # 모든노드를 방문했다면
        return 0

    if dp[cur][visit] != 9999999:  # 메모이제이션 해놓은 값이 있다면?
        return dp[cur][visit]

    for i in range(N):  # 처음 저장하는 경우라면 모든 노드를 순회
        bit = 1 << i
        if visit & bit:  # 이미 방문한 노드라면 skip
            continue
        dp[cur][visit] = min(dp[cur][visit], recur(cur + 1, visit | bit) + arr[cur][i])

    return dp[cur][visit]


print(recur(0, 0))