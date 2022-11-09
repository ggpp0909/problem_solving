import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

for k in range(1, n+1):
    leng = int(input())

    arr = [list(map(int, input().split())) for i in range(leng)]

    arr_180 = [[0]*leng for i in range(leng)]
    arr_90 = [[0]*leng for i in range(leng)]
    arr_270 = [[0]*leng for i in range(leng)]
    for i in range(leng):
        for j in range(leng):
            arr_180[i][j] = arr[leng-i-1][leng-j-1]
            arr_90[i][j] = arr[leng-j-1][i]
            arr_270[i][j] = arr[j][leng-i-1]

    print('#{}'.format(k))
    for i in range(leng):
        print(*arr_90[i], sep='', end='')
        print(' ', end='')
        print(*arr_180[i], sep='', end='')
        print(' ', end='')
        print(*arr_270[i], sep='', end='')
        print()

