import sys
sys.stdin = open('input.txt')

tc = int(input())
for k in range(1, tc + 1):
    N = float(input())

    two_inverse = 1/2
    temp = 0
    arr = []
    flag = 0
    for i in range(1, 13):
        if temp + two_inverse ** i <= N:
            temp += two_inverse ** i
            arr.append(1)
            if temp == N:
                flag = 1
                break
        else:
            arr.append(0)

    if flag:
        ans = ''
        for i in arr:
            ans += str(i)
    else:
        ans = 'overflow'

    print('#{} {}'.format(k, ans))

