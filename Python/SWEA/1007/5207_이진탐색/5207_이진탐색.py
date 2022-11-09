import sys
sys.stdin = open('input.txt')

def bs(n):
    global cnt

    s = 0
    e = len(arr_A) - 1
    flag = 0

    while s <= e:
        mid = (s + e) // 2

        if arr_A[mid] == n:
            cnt += 1
            return

        elif arr_A[mid] < n: # 값이 오른쪽에 있음
            if flag == -1: # flag 왼쪽 오른쪽 번갈아가면서
                return
            flag = -1
            s = mid + 1

        else: # 값이 왼쪽에 있음
            if flag == 1:
                return
            flag = 1
            e = mid - 1

T = int(input())

for k in range(1, T + 1):
    N, M = map(int, input().split())
    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))

    arr_A.sort()
    cnt = 0
    for i in arr_B:
        bs(i)

    print('#{} {}'.format(k, cnt))

