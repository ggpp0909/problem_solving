from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


# 상어위치찾기
shark_i = 0
shark_j = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark_i = i
            shark_j = j
            arr[i][j] = 0
            break

time = 0
sharksize = 2  # 현재 상어 사이즈
stomach = 0  # 상어 뱃속 (먹은물고기수)


def find():
    global sharksize, stomach, time, shark_i, shark_j
    visited = [[False for i in range(N)] for j in range(N)]
    que = deque()
    que.append([shark_i, shark_j, False])  # 세번째 인자는 물고기 위치인지 아닌지
    visited[shark_i][shark_j] = True
    depth = 0

    while que:
        size = len(que)

        for _ in range(size):
            x, y, is_fish = que.popleft()

            for dir in range(4):
                nx = x + di[dir]
                ny = y + dj[dir]

                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] <= sharksize:
                    visited[nx][ny] = True
                    is_fish = True
                    if arr[nx][ny] == 0:
                        is_fish = False

                    que.append([nx, ny, is_fish])
        depth += 1
        flag = False
        temp_arr = sorted(list(que), key=lambda x: (x[0], x[1]))
        # print(temp_arr)
        for i in range(len(temp_arr)):
            if temp_arr[i][2] and arr[temp_arr[i][0]][temp_arr[i][1]] < sharksize:  # 물고기라면
                arr[temp_arr[i][0]][temp_arr[i][1]] = 0
                shark_i = temp_arr[i][0]
                shark_j = temp_arr[i][1]
                stomach += 1
                time += depth
                if sharksize == stomach:  # 크기만큼 먹었어? 상어크기 업
                    sharksize += 1
                    stomach = 0
                flag = True
                break
        if flag:
            return
    print(time)
    exit()


while True:
    find()
