import sys
sys.stdin = open('input.txt')

tc = int(input())

di = [1, 0] # 어차피 오른쪽, 아래로만 갈거임
dj = [0, 1]

def recur(i, j, tot):
    global ans
    if i == n - 1 and j == n - 1:   # 도착했으면 비교해서 큰거로 바꿔
        ans = min(ans, tot)
        return

    if tot > ans:   # 가는 도중에 ans보다 커지면 돌아가(가지치기)
        return

    for dir in range(2):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < n and 0 <= nj < n:
            recur(ni, nj, tot + arr[ni][nj])    # 가는 길마다 값 저장하면서 들어가기

for k in range(1, tc + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    ans = 100000

    recur(0, 0, arr[0][0])
    print('#{} {}'.format(k, ans))

