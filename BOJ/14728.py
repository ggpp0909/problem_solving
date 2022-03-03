N, T = map(int, input().split()) # 냅색, N은 물건수, T는 배낭의 무게
arr = [[0, 0]] + [list(map(int, input().split())) for i in range(N)]
dp = [[0 for i in range(T + 1)] for j in range(N + 1)]
# print(arr)
# i번재 물건까지 봤을때 최대가치를 dp에 저장
for i in range(1, N + 1):
    # 배낭 무게가 j일 때
    for j in range(1, T + 1):
        w = arr[i][0]
        v = arr[i][1]

        # 만일 물건 무게가 배낭무게보다 크다면 배낭에 못넣으므로 이전값 가져오기
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else: # 지금 물건을 담거나 안담거나, (담는다면 지금 담을 무게만큼 뺀 배낭수용무게에 저장된 값에 현재가치 더하기)
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][T])