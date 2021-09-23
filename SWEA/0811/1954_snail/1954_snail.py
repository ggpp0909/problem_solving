import sys
sys.stdin = open('input.txt')

n = int(input())

for k in range(1, n + 1):
    length = int(input())

    # 방향벡터 선언, 달팽이처럼 돌기위해 우, 하, 좌, 상순서
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 배열 초기화
    arr = [[0]*length for i in range(length)]

    dir_idx = 0  # 방향벡터 첫 인덱스
    i = j = 0  # 시작 위치
    num = 1
    arr[i][j] = 1
    while True:
        if num == length ** 2: # 종료조건, 모든칸 다 채웠으면 나와
            break
        ni = i + di[dir_idx]    # 한칸 진행
        nj = j + dj[dir_idx]
        # 범위 벗어나거나 0이 아닌 숫자 만나면 돌아 like 달팽이.
        if 0 <= ni < length and 0 <= nj < length and arr[ni][nj] == 0:
            num += 1
            arr[ni][nj] = num  # 숫자 채우기
            i = ni
            j = nj
        else:
            dir_idx = (dir_idx + 1) % 4

    print('#{}'.format(k))
    for i in arr:
        print(*i)
