import sys
sys.stdin = open('input.txt')

n = int(input())

for k in range(1, n+1):
    # K = 한번충전으로 이동가능한 정류장수 , N = 종점, M = 충정기정류장 수
    K, N, M = map(int, input().split())
    charge_idx = list(map(int, input().split()))

    charge = [0 for i in range(N+1)] # 종점까지 충전소 세팅하기  0없음, 1있음
    for i in charge_idx:
        charge[i] = 1

    cnt = 0
    fuel = K + 1  # for문 처음 시작할때 -1 하므로
    for i in range(N + 1): # 버스 출발!
        if i == N:   # 도착하면 끝 아무것도 하지마
            break
        fuel -= 1
        # print(fuel)
        if fuel == 0:  # 기름이 다닳은 시점에서 그전 K안에 정류장이 있었나 검사.
            temp =0  # 다 닳은 시점에서 몇정거장 전에 충전소 있었는지
            for j in range(i, i-(K+1), -1):
                if temp == K:
                    cnt = 0
                    break
                if charge[j] == 1:
                    fuel = K - temp # 현위치에서 남은 연료량
                    cnt += 1  # 충전횟수 + 1
                    break
                else:
                    temp += 1  # for문 돌면서

    print('#{} {}'.format(k, cnt))

