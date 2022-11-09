# from copy import deepcopy
#
# N, M = map(int, input().split())
# arr = [list(input()) for i in range(N)]
# ans = -1
#
# def rotate(arr):   # 보드판 반시계 90도 회전
#     temp = [[0] * M for i in range(N)]
#     for i in range(N):
#         for j in range(M):
#             temp[N - 1 - j][i] = arr[i][j]
#     return temp
#
# def move(Ri, Rj, Bi, Bj, Oi, Oj): # 윗방향으로 구슬 굴리기 (벽이나 구멍 앞에 구슬 올때 까지
#     is_end = 0
#     tempRi = Ri
#     tempBi = Bi
#
#     while True:
#         nBi = Bi - 1
#         nRi = Ri - 1
#
#         # 둘다 갈수 있으면 한칸씩 올려
#         if arr[nRi][Rj] != '#' and arr[nBi][Bj] != '#' and arr[nRi][Rj] != 'O' and arr[nBi][Bj] != 'O':
#             arr[Ri][Rj] = '.'
#             arr[Bi][Bj] = '.'
#             arr[nRi][Rj] = 'R'
#             arr[nBi][Bj] = 'B'
#             Ri -= 1
#             Bi -= 1
#
#         # 빨간 구슬만 벽이나 구멍 만났다면?
#         elif (arr[nRi][Rj] == '#' and arr[nBi][Bj] != '#') or (arr[nRi][Rj] == 'O' and arr[nBi][Bj] != 'O'):
#             # 파란구슬이 빨간구슬 뒤에있지않을때 또는 벽앞 아니면 올려
#             if arr[nBi][Bj] != 'R':
#                 arr[Bi][Bj] = '.'
#                 arr[nBi][Bj] = 'B'
#                 Bi -=1
#             else:
#                 is_end = 1
#         # 파란 구슬만 벽에 만났다면?
#         elif (arr[nRi][Rj] == '#' and arr[nBi][Bj] != '#') or (arr[nRi][Rj] == 'O' and arr[nBi][Bj] != 'O'):
#             # 파란구슬이 빨간구슬 뒤에있지않을때 또는 벽앞 아니면 올려
#             if arr[nBi][Bj] != 'R':
#                 arr[Bi][Bj] = '.'
#                 arr[nBi][Bj] = 'B'
#                 Ri -= 1
#             else:
#                 is_end = 1
#         # 둘다 벽이나 구멍에 만났다면?
#         elif arr[nRi][Rj] == '#' or arr[nBi][Bj] == '#' or arr[nRi][Rj] == 'O' or arr[nBi][Bj] == 'O':
#             is_end = 1
#
#         if Ri == Bi and  Rj == Bj: # 두 구슬이 같은 위치에 있으면?
#             if tempBi > tempRi: # 파란구슬이 더 밑에있었으면 파란구슬 빠꾸
#                 arr[Bi][Bj] = '.'
#                 arr[nBi][Bj] = 'B'
#
#
#             else:
#
#     return
#
#
# def dfs(arr, cnt):
#     if cnt == 10:
#         return
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 'R':
#                 Ri, Rj = i, j
#             elif arr[i][j] == 'B':
#                 Bi, Bj = i, j
#             elif arr[i][j] == 'O':
#                 Oi, Oj = i, j
#
#     move(Ri, Rj, Bi, Bj, Oi, Oj)
#
#     for i in range(4):
#         temp = deepcopy(rotate())
#         dfs(temp, cnt + 1)
#
#     pass

#######################################################
# https://wlstyql.tistory.com/72?category=852442 참고 #
#######################################################

from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)] # 빨간구슬, 파란구슬의 좌표 -> 4차원 배열

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            Ri, Rj = i, j
        elif arr[i][j] == 'B':
            Bi, Bj = i, j

que = deque()
que.append((Ri, Rj, Bi, Bj, 1)) # 두구슬 좌표, depth
visited[Ri][Rj][Bi][Bj] = True

def move(i, j, di, dj): # 구슬을 벽 or 구멍 앞까지 굴린다
    cnt = 0
    while arr[i + di][j + dj] != '#' and arr[i][j] != 'O':
        i += di
        j += dj
        cnt += 1
    return i, j, cnt

while que:
    ri, rj, bi, bj, depth = que.popleft()

    if depth > 10: # 10번안에 성공못하면
        print(-1)
        exit()

    for dir in range(4):
        nri, nrj, rcnt = move(ri, rj, di[dir], dj[dir])  # 빨간구슬 굴려
        nbi, nbj, bcnt = move(bi, bj, di[dir], dj[dir])  # 파란구슬 굴려
        if arr[nbi][nbj] != 'O': # 파란구슬이 구멍에 들어가지 않는다면 (현재 파란구슬이 벽앞에 위치했다면, 실패 X)
            if arr[nri][nrj] == 'O': # 빨간구슬이 들어간다? 성공
                print(depth)
                exit()

            if nri == nbi and nrj == nbj:  # 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다
                if rcnt > bcnt:  # 이동거리가 많은 것을 한칸 뒤로
                    nri -= di[dir]
                    nrj -= dj[dir]
                else:
                    nbi -= di[dir]
                    nbj -= dj[dir]

            if visited[nri][nrj][nbi][nbj]:
                continue
            visited[nri][nrj][nbi][nbj] = True
            que.append((nri, nrj, nbi, nbj, depth + 1))

# 10번 까지 안가고 que가 비게되어 끝난다면
print(-1)
