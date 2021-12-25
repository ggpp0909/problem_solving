n = int(input())
cost = []
for i in range(n):
    a = list(map(int, input().split()))
    cost.append(a)

visited = [False for i in range(n)]
dp = [[999999999999 for i in range(n)] for j in range(1 << 16)]


visited[0] = True  # 0번도시에서 출발


def dfs(cur, cnt):
    global tot, ans

    if cnt == n and cost[cur][0] != 0:  # 마지막 0번으로 귀환
        if dp[cur][0]:
            return dp[cur][0]
        else:
            return 999999999999

    visit = 1 << cur

    for i in range(n):
        if visited[i]:  # 들렀던 도시라면 패스
            continue
        if dp[cur][visit]:
            continue
        elif cur != i and cost[cur][i] != 0:  # 현재 있는 도시 무시, 비용이 0인도시 무시
            visited[i] = True  # i도시로 ㄱㄱ, 요금에 i로 가는 요금 추가
            tot += cost[cur][i]
            dfs(i, cnt + 1)
            tot -= cost[cur][i]  # 다 돌아서 ans에 값저장후 리턴했으면 요금 빼주기
            visited[i] = False

    return ans


print(dfs(0, 1))