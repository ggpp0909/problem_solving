# n = int(input())
# arr = [list(map(int, input().split())) for i in range(n)]
# visited = [False for i in range(5)]
# ans = 0
#
# def recur(cur, cnt, total):
#     global ans
#
#     if cnt == 5:
#         ans = max(ans, total)
#         return
#
#     if cur == n:
#         return
#
#     recur(cur + 1, cnt, total)
#     for i in range(5):
#         if visited[i]:
#             continue
#
#         visited[i] = True
#         recur(cur + 1, cnt + 1, total + arr[cur][i])
#         visited[i] = False
#
# recur(0, 0, 0)
#
# print(ans)


import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
dp = [[-1 for i in range(1 << 5)] for j in range(N)]

# 4번 템플릿 기반
def recur(cur, visit):
    if visit == (1 << 5) - 1:
        return 0

    if cur == N:
        return -10000000000 # 1번조건문에서 걸리지않고 모든사람을 다봤다면 큰음수넣어서 밑에 max에서 안걸리도록

    if dp[cur][visit] != -1: # 메모이제이션
        return dp[cur][visit]


    ret = recur(cur + 1, visit) # cur번째 사람을 안고르고 지나치는경우
    # cur 번째 사람을 고를경우
    for i in range(5):
        if visit & (1 << i): # i번째 사람이 이미 다른 능력을 쓰고있다면
            continue
        ret = max(ret, recur(cur + 1, visit | (1 << i)) + arr[cur][i])
        dp[cur][visit] = ret # 메모이제이션
    return ret

print(recur(0, 0))