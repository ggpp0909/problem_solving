import sys
sys.stdin = open('input.txt')

tc = int(input())

for k in range(1, tc + 1):
    N, M = map(int, input().split())

    flag = 1
    for i in range(N):
        if M & (1 << i) == 0:
            flag = 0
            break

    if flag:
        ans = 'ON'
    else:
        ans = 'OFF'

    print('#{} {}'.format(k, ans))