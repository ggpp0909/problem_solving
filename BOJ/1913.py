N = int(input())
num = int(input())

arr = [[1 for i in range(N)] for j in range(N)]

pi, pj = N // 2, N // 2
l, r, t, b = N // 2, N // 2, N // 2, N // 2

while pi != 0 and pj != 0:
    # 한칸올리기
    t -= 1
    pi -= 1
    arr[pi][pj] += arr[pi + 1][pj]

    # 오른쪽으로 가기
    r += 1
    while pj < r:
        pj += 1
        arr[pi][pj] += arr[pi][pj - 1]

    # 아래으로 가기
    b += 1
    while pi < b:
        pi += 1
        arr[pi][pj] += arr[pi - 1][pj]

    # 왼쪽으로 가기
    l -= 1
    while pj > l:
        pj -= 1
        arr[pi][pj] += arr[pi][pj + 1]

    # 위쪽으로 가기
    while pi > t:
        pi -= 1
        arr[pi][pj] += arr[pi + 1][pj]

for i in arr:
    print(*i)

for i in range(N):
    for j in range(N):
        if arr[i][j] == num:
            print(i + 1, j + 1)