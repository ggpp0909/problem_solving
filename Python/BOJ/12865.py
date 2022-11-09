# import sys

# N, K = map(int, sys.stdin.readline().rstrip().split())
# WV = []

# for i in range(N):
#     w, v = map(int, sys.stdin.readline().rstrip().split())
#     WV.append([w, v])

# dp = [0 for i in range(K + 1)]
# visited = [[] for i in range(K + 1)]

# for i in range(1, K + 1):
#     for j in range(N):
#         if i >= WV[j][0]:
#             if j in visited[i - WV[j][0]]:
#                 continue
#             if dp[i] <= dp[i - WV[j][0]] + WV[j][1]:
#                 dp[i] = dp[i - WV[j][0]] + WV[j][1]
#                 visited[i] = visited[i - WV[j][0]][:]
#                 visited[i].append(j)

# print(max(dp))



n, k = map(int, input().split())

dp = [0 for i in range(k + 1)]

for i in range(1, n + 1):
    a, b = map(int, input().split())

    for j in range(k, 0, -1):
        if j >= a:
            dp[j] = max(dp[j], dp[j - a] + b)

print(dp[-1])