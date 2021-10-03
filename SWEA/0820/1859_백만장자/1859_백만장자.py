import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())
for k in range(1, n+1):
    num = int(input())
    arr = list(map(int, input().split()))

    temp = arr[-1]
    ans = 0
    for i in range(num-1, -1, -1):
        if arr[i] >= temp:
            temp = arr[i]
        else:
            ans += temp - arr[i]

    print('#{} {}'.format(k, ans))
