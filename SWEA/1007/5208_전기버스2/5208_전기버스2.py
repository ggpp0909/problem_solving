import sys
sys.stdin = open('input.txt')

def recur(idx, cnt):
    global ans

    if idx >= len(arr):     # 종점이야? 갱신해
        ans = min(ans, cnt)
        return

    if cnt >= ans:
        return

    for i in range(1, arr[idx] + 1):    # idx는 현재위치, 현재위치의 연료만큼 한칸씩 가면서 충전, 완탐
        recur(idx + i, cnt + 1)     # 다음 위치, 충전횟수


T = int(input())

for k in range(1, T + 1):
    temp = list(map(int, input().split()))
    arr = temp[1:] # n - 1개이므로 기저조건 주의

    ans = 10000000000
    recur(0, 0)

    print('#{} {}'.format(k, ans - 1))
