N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)] # 물의양 지도
cloud = [[N - 1, 0], [N - 2, 0], [N - 1, 1], [N - 2, 1]] #구름 좌표
exist = [[False for i in range(N)] for j in range(N)] # 구름 존재 지도

di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def make_exist(): # cloud로 exist만드는 함수
    for i in range(N):
        for j in range(N):
            exist[i][j] = False # 초기화

    for i in cloud:
        exist[i[0]][i[1]] = True

def make_cloud(): # exist로 cloud 만드는 함수
    global cloud

    cloud = []
    for i in range(N):
        for j in range(N):
            if exist[i][j]:
                cloud.append([i, j])

make_exist()

def move(d, s):
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + di[d] * s + 100*N) % N
        cloud[i][1] = (cloud[i][1] + dj[d] * s + 100*N) % N
    make_exist()

def rain():
    for i in range(len(cloud)):
        arr[cloud[i][0]][cloud[i][1]] += 1

def water():
    global arr
    arr2 = []
    for i in arr:
        arr2.append(i.copy())
    # 복사해놓고 탐색과 반영을 따로함
    for i in range(N):
        for j in range(N):
            if exist[i][j]:
                cnt = 0
                for k in range(2, 9, 2):
                    ni = i + di[k]
                    nj = j + dj[k]

                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]:
                        cnt += 1
                arr2[i][j] += cnt
    arr = []
    for i in arr2:
        arr.append(i.copy())

def cloud_():
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not exist[i][j]:
                exist[i][j] = True
                arr[i][j] -= 2
            else:
                exist[i][j] = False

    make_cloud()

for i in range(M):
    d, s = map(int, input().split())
    move(d, s)
    rain()
    water()
    cloud_()

ans = 0
for i in range(N):
    for j in range(N):
        ans += arr[i][j]

print(ans)