import math
from pprint import pprint
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

# 하 우 상 좌 (반시계)
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
# 뒤돌기 -> (dir + 2) % 4
# 좌회전 -> (dir + 1) % 4
# 우회전 -> (dir + 3) % 4

def is_insquare(i, j): # i, j가 격자안인지 확인하는 함수
    return 0 <= i < N and 0 <= j < N

def wind(idx, i, j): # 방향벡터인덱스, i, j는 토네이도의 이동지점
    global ans
    
    rate_1 = math.floor(arr[i][j] * (0.01))
    rate_2 = math.floor(arr[i][j] * (0.02))
    rate_5 = math.floor(arr[i][j] * (0.05))
    rate_7 = math.floor(arr[i][j] * (0.07))
    rate_10 = math.floor(arr[i][j] * (0.1))
    alpha = arr[i][j] - 2 * (rate_1 + rate_2 + rate_7 + rate_10) - rate_5

    # 5% -> 진행방향 두칸
    ti, tj = i + 2 * di[idx], j + 2 * dj[idx]
    if is_insquare(ti, tj):
        arr[ti][tj] += rate_5
    else: ans += rate_5

    # alpha -> 진행방향 한칸
    ti, tj = i + di[idx], j + dj[idx]
    if is_insquare(ti, tj):
        arr[ti][tj] += alpha
    else: ans += alpha

    # 10% -> 진행방향 한칸후 각각 좌, 우 한칸
    li, lj = ti + di[(idx + 1) % 4], tj + dj[(idx + 1) % 4]
    ri, rj = ti + di[(idx + 3) % 4], tj + dj[(idx + 3) % 4]
    if is_insquare(li, lj):
        arr[li][lj] += rate_10
    else: ans += rate_10

    if is_insquare(ri, rj):
        arr[ri][rj] += rate_10
    else: ans += rate_10

    # 7% -> 제자리 좌 우 한칸씩
    li, lj = i + di[(idx + 1) % 4], j + dj[(idx + 1) % 4]
    ri, rj = i + di[(idx + 3) % 4], j + dj[(idx + 3) % 4]
    if is_insquare(li, lj):
        arr[li][lj] += rate_7
    else: ans += rate_7

    if is_insquare(ri, rj):
        arr[ri][rj] += rate_7
    else: ans += rate_7

    # 2% -> 제자리 좌 우 2칸씩
    li, lj = i + 2 * di[((idx + 1) % 4)], j + 2 * dj[((idx + 1) % 4)]
    ri, rj = i + 2 * di[((idx + 3) % 4)], j + 2 * dj[((idx + 3) % 4)]
    if is_insquare(li, lj):
        arr[li][lj] += rate_2
    else: ans += rate_2

    if is_insquare(ri, rj):
        arr[ri][rj] += rate_2
    else: ans += rate_2

    # 1% -> 뒤로 한칸 후 각각 좌 우 한칸
    ti, tj = i + di[(idx + 2) % 4], j + dj[(idx + 2) % 4] # 뒤로 한칸
    li, lj = ti + di[(idx + 1) % 4], tj + dj[(idx + 1) % 4]
    ri, rj = ti + di[(idx + 3) % 4], tj + dj[(idx + 3) % 4]
    if is_insquare(li, lj):
        arr[li][lj] += rate_1
    else: ans += rate_1

    if is_insquare(ri, rj):
        arr[ri][rj] += rate_1
    else: ans += rate_1

    arr[i][j] = 0

L = N // 2 - 1
R = N // 2 + 1
T = N // 2 - 1
B = N // 2 + 1
ans = 0
# temp = [[0 for i in range(N)] for j in range(N)]
# cnt = 1
while L != -1:
    # 처음 왼쪽으로 한칸 진행
    wind(3, T + 1, L)
    # temp[T + 1][L] = cnt
    # cnt += 1

    # B 만날때까지 아래로 토네이도 이동
    for i in range(T + 2, B + 1):
        wind(0, i, L)
        # temp[i][L] = cnt
        # cnt += 1

    # R 만날때까지 오른쪽으로 토네이도 이동
    for i in range(L + 1, R + 1):
        wind(1, B, i)
        # temp[B][i] = cnt
        # cnt += 1

    # T 만날때까지 위로 토네이도 이동
    for i in range(B - 1, T - 1, -1):
        wind(2, i, R)
        # temp[i][R] = cnt
        # cnt += 1

    # L 만날때까지 왼쪽으로 토네이도 이동
    for i in range(R - 1, L - 1, -1):
        wind(3, T, i)
        # temp[T][i] = cnt
        # cnt += 1
    
    L -= 1
    R += 1
    T -= 1
    B += 1

print(ans)

# pprint(temp)

