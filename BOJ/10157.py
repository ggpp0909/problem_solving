C, R = map(int, input().split())
K = int(input())

if C * R < K:
    print(0)
    exit()

stage = [[0 for i in range(C)] for j in range(R)]
# 하 우 상 좌
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
dir_idx = 0  
i = j = 0
num = 0
ai = aj = 0
while num < C * R:
    num += 1
    if num == K: 
        ai = i + 1
        aj = j + 1
        break

    stage[i][j] = num  
    ni = i + di[dir_idx]
    nj = j + dj[dir_idx]
    if 0 <= ni < R and 0 <= nj < C and stage[ni][nj] == 0:
        i = ni
        j = nj
    else:
        dir_idx = (dir_idx + 1) % 4
        i += di[dir_idx]
        j += dj[dir_idx]

print(aj, ai)