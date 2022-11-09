import sys
sys.stdin = open('input.txt')

n = int(input())

for k in range(1, n+1):
    P, A, B = map(int, input().split())
    A_s = B_s = 1
    A_e = B_e = P

    A_cnt = 0
    #A
    while A_s <= A_e:
        mid = (A_s + A_e) // 2
        A_cnt += 1
        if mid == A:
            break
        elif A > mid:
            A_s = mid
        else:
            A_e = mid

    B_cnt = 0
    #B
    while B_s <= B_e:
        mid = (B_s + B_e) // 2
        B_cnt += 1
        if mid == B:
            break
        elif B > mid:
            B_s = mid
        else:
            B_e = mid

    if A_cnt == B_cnt:
        ans = '0'
    elif A_cnt < B_cnt:
        ans = 'A'
    else:
        ans = 'B'

    print('#{} {}'.format(k, ans))
