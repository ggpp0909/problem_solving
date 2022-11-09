import sys
sys.stdin = open('input.txt')

for _ in range(10):
    k = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    ans = sum(arr[0]) # 일단 첫번째 행의 sum으로 초기화
    # ans는 최댓값이 나오는 순간 값을 update 한다.

    # 행 우선 탐색
    for i in range(len(arr)):
        temp = sum(arr[i])
        if temp > ans:
            ans = temp

    # 열 우선 탐색
    for i in range(len(arr)):
        temp = 0
        for j in range(len(arr[i])):
            temp += arr[j][i]
        if temp > ans:
            ans = temp

    # 대각선 우측아래방향
    temp = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                temp += arr[i][j]
    if temp > ans:
        ans = temp

    # 대각선 좌측아래방향
    temp = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])-1,-1,-1): # 열 순서만 거꾸로, 위와동일
            if i == j:
                temp += arr[i][j]
    if temp > ans:
        ans = temp

    print('#{} {}'.format(k, ans))


