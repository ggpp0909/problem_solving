import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
prefix = [[0 for i in range(M + 1)] for j in range(N + 1)]

# # 가로 세로 첫째줄 처리
# prefix[0][0] = arr[0][0]

# for i in range(1, M):
#     prefix[0][i] = prefix[0][i - 1] + arr[0][i]

# for i in range(1, N):
#     prefix[i][0] = prefix[i - 1][0] + arr[i][0]

# print(prefix)

# 나머지 줄 처리
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1] + arr[i - 1][j - 1] # arr은 사실 i, j인데 range때매 저렇게 함

# print(prefix)
ans = -9999999999
for i in range(1, N + 1):
    for j in range(1, M + 1):
        for k in range(i, N + 1):
            for l in range(j, M + 1):
                ans = max(ans, prefix[k][l] - prefix[k][j - 1] - prefix[i - 1][l] + prefix[i - 1][j - 1])
print(ans)