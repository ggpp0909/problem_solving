# n = int(input())
# visited = [False for i in range(n)]
# visited2 = [False for i in range(3 * n)] #/
# visited3 = [False for i in range(3 * n)] #\
#
# cnt = 0
# def recur(cur=0):
#     global cnt
#
#     if cur == n:
#         cnt += 1
#         return
#
#     for i in range(n):
#         if visited[i] or visited2[cur + i] or visited3[n + cur - i]:
#             continue
#
#         visited[i] = True
#         visited2[cur + i] = True
#         visited3[n + cur - i] = True
#         recur(cur + 1)
#         visited[i] = False
#         visited2[cur + i] = False
#         visited3[n + cur - i] = False
#
# recur()
# print(cnt)


# 211226 재풀이
N = int(input())
ans = 0
visited_col = [False for i in range(N)]
visited_ld = [False for i in range(3 * N)] # 대각선의 인덱스 최대 2N까지 할것이므로
visited_rd = [False for i in range(3 * N)]

# 왼쪽 위 -> 아래로 가는 대각선의 요소 특징 -> 행 - 열 이 같음 (or 열 - 행)
# 오른쪽 위 -> 아래로 가는 대각선 요소 특징 -> 행 + 열 이 같음

def recur(cur, N):
    global ans

    if cur == N:
        ans += 1
        return

    for i in range(N):  # 여기서 cur은 행, i는 열을 의미
        if visited_col[i] or visited_ld[N + (cur - i)] or visited_rd[cur + i]:
            continue

        visited_col[i] = True
        visited_ld[N + (cur - i)] = True
        visited_rd[cur + i] = True
        recur(cur + 1, N)
        visited_col[i] = False
        visited_ld[N + (cur - i)] = False
        visited_rd[cur + i] = False

recur(0, N)
print(ans)