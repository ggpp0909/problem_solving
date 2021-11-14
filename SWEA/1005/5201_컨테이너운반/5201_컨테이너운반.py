import sys
sys.stdin = open('input.txt')

T = int(input())

for k in range(1, T + 1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    visited = [False for i in range(N)] # 실은 화물은 저장
    T = list(map(int, input().split()))
    W.sort(reverse=True)    # 그리디, 무조건 무게 높은거 우선으로 실어
    T.sort(reverse=True)

    ans = 0
    for i in range(len(T)):
        for j in range(len(W)):
            if W[j] <= T[i] and not visited[j]:
                ans += W[j]
                visited[j] = True    # 실었으면 표시하고 다음트럭 출동해
                break

    print('#{} {}'.format(k, ans))
