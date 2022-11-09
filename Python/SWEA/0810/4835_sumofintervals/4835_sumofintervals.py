import sys
sys.stdin = open('input.txt')

n = int(input())

for k in range(1, n+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    Max = 0
    Min = 99999999999999999999999
    for i in range(N - M + 1): # 인덱스 에러 방지
        temp = 0
        for j in range(i, i+M):
            temp += arr[j]

        if temp > Max:
            Max = temp

        if temp < Min:
            Min = temp

    result = Max - Min

    print('#{} {}'.format(k, result))