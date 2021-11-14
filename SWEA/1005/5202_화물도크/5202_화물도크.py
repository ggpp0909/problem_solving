import sys
sys.stdin = open('input.txt')

T = int(input())

for k in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    arr.sort(key=lambda x: x[1]) # 그리디, 종료시간기준 정렬, 무조건 빨리 끝나는거 우선으로 스케줄을 짜

    cnt = 1
    temp = arr[0][1] #종료시간
    for i in range(len(arr) - 1):
        if temp <= arr[i + 1][0]: # 현재 작업 종료시간 <= 다음 시작시간이면 작업 이어서 가능
            cnt += 1    # 작업횟수 늘려
            temp = arr[i + 1][1] # 현재작업의 종료시간 갱신

    print('#{} {}'.format(k, cnt))