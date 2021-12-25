import sys
from pprint import pprint
sys.stdin = open('input.txt')
# 딥카피 이슈 해결 못함

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def crush(power, i, j, n_arr):
    global H, W
    visited[i][j] = True
    for k in range(1, power):
        for dir in range(4):
            ni = i + di[dir] * k
            nj = j + dj[dir] * k
            if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] == False:
                crush(n_arr[ni][nj], ni, nj, n_arr)
    return

def pull(n_arr):
    for i in range(H - 1, -1, -1):
        for j in range(W):
            if visited[i][j]:
                temp = i - 1
                while temp >= 0 and visited[temp][j]:  # temp 가 범위밖으로 안나가면서,
                    temp -= 1

                if temp < 0:  # 맨 위까지 올라갔을때까지 없다면
                    n_arr[i][j] = 0
                else:
                    n_arr[i][j] = n_arr[temp][j]
                    visited[temp][j] = True
    return

def play(N, arr):
    global ans

    if N == 0:
        tot = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                    tot += 1
        ans = min(ans, tot)
        # print(ans)
        return

    for i in range(W):
        visited = [[False for i in range(W)] for j in range(H)]
        n_arr = [i[:] for i in arr]
        start_j = 0
        for j in range(H):
            if n_arr[j][i] != 0:
                start_j = j
                break
        if start_j:
            crush(n_arr[start_j][i], start_j, i, n_arr)
            pull(n_arr)
            pprint(n_arr)
            # print(ans)
            play(N - 1, n_arr)

T = int(input())

for k in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(H)]
    visited = [[False for i in range(W)] for j in range(H)]

    # print(arr)
    ans = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                ans += 1

    play(N, arr)

    print(ans)


