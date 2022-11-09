import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

for k in range(1, n + 1):
    temp = [input() for i in range(5)]

    leng = 5
    for i in temp:
        if len(i) > leng:
            leng = len(i)

    arr = [[''] * leng for i in range(5)]

    for i in range(5):
        for j in range(len(temp[i])):
            arr[i][j] = temp[i][j]

    ans = ''
    for i in range(leng):
        for j in range(5):
            ans += arr[j][i]

    print('#{} {}'.format(k, ans))
