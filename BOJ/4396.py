# 주위 8방향 지뢰개수 세기
def check(i, j):
    cnt = 0
    for dir in range(8):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < n and 0 <= nj < n:
            if before[ni][nj] == '*':
                cnt += 1
    return cnt

di = [1, 0, -1, 0, 1, 1, -1, -1]
dj = [0, 1, 0, -1, -1, 1, 1, -1]


n = int(input())

before = [input() for i in range(n)]
played = [input() for i in range(n)]
ans = [['.' for i in range(n)] for j in range(n)]

# 지뢰밟음?
flag = 0

for i in range(n):
    for j in range(n):
        if played[i][j] == 'x' and before[i][j] == '.':
            ans[i][j] = check(i, j)
        elif played[i][j] == 'x' and before[i][j] == '*':
            flag = 1

if flag:
    for i in range(n):
        for j in range(n):
            if before[i][j] == '*':
                ans[i][j] = '*'

for i in range(n):
    print(*ans[i], sep='')
