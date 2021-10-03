import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())
for k in range(1, n+1):
    arr = [list(map(int, input().split())) for i in range(9)]
    flag = 0
    for i in range(9): # 가로 세로 동시 탐색
        check_row = [0 for i in range(10)]
        check_col = [0 for i in range(10)]
        for j in range(9):
            check_row[arr[i][j]] = 1
            check_col[arr[j][i]] = 1
        for l in range(1,10):
            if check_row[l] == 0 or check_col[l] == 0: # 안되는 경우 발견시 케이스 바로종료
                flag = 1
                break
    if flag:
        print('#{} {}'.format(k, 0))
        continue

    # 격자 탐색
    for i in range(0,9,3):
        for j in range(0, 9, 3):
            check_box = [0 for i in range(10)]
            for l in range(3):
                for o in range(3):
                    check_box[arr[i+l][j+o]] = 1
            for j in range(1,10):
                if check_box[j] == 0: # 안되는 경우 발견시 케이스 바로종료
                    flag = 1
                    break
    if flag:
        print('#{} {}'.format(k, 0))
    else:
        print('#{} {}'.format(k, 1)) # flag가 여전히 0, 즉 모든 조건만족할 경우 1출력



