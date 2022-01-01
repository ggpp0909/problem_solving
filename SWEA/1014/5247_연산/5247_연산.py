import sys
from collections import deque
sys.stdin = open('input.txt')

# BFS, 백준 숨바꼭질과 같은 로직

T = int(input())

for k in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [False for i in range(1000001)]
    que = deque()

    que.append([N, 0]) # 현재 위치와 depth를 que에 같이 넣음 (BFS에서는 depth를 알기 힘들기 때문에)
    visited[N] = True

    while que:
        temp, cnt = que.popleft()
        if temp == M: # 찾았어? 프린트해
            print('#{} {}'.format(k, cnt))
            break

        for i in [temp + 1, temp - 1, 2 * temp, temp - 10]:  # 현재 위치에서 갈 수 있는 곳들 조건 만족하면 전부 큐에 넣어
            if 1 <= i <= 1000000 and visited[i] == False:
                visited[i] = True
                que.append([i, cnt + 1])
