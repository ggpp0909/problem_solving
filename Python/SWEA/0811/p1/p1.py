import sys
sys.stdin = open('input.txt')

n = int(input())

for k in range(1, n+1):
    length = int(input())
    arr = [list(map(int,input().split())) for i in range(length)]

    # 방향벡터, 오른쪽부터 시계방향
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    ans = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for l in range(4):  # 방향벡터를 이용하여 인접한 좌표를 구함
                ni = i + di[l]
                nj = j + dj[l]
                # 인접한 좌표가 범위 안에 있을때만 ans에 누적
                if 0 <= ni < length and 0 <= nj < length:
                    ans += abs(arr[i][j] - arr[ni][nj])

    print('#{} {}'.format(k, ans))
