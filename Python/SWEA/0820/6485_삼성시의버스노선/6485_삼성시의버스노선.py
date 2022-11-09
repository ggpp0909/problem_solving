import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

for k in range(1, n+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    P = int(input())
    C = [0 for i in range(5001)]
    temp = [int(input()) for i in range(P)]
    temp2 = list(set(temp))

    for i in temp2:
        for j in arr:
            if j[0] <= i <= j[1]:
                C[i] += 1

    print('#{}'.format(k), end=' ')
    for i in temp:
        print(C[i], end=' ')
    print()
