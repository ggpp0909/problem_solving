import sys
sys.stdin = open('input.txt')

def recur(cur, n, tot):
    global ans

    if cur == n: # 기저 왔으면 갱신
        ans = min(ans, tot)
        return

    if tot >= ans: # 가지치기
        return

    for i in range(n): # i 열을 하나하나 보겠다는거고, cur 행을 하나하나보겠다는거
        if visited[i]: # 쓴 열은 쓰지마
            continue
        visited[i] = True # 이거 쓸거야
        recur(cur + 1, n, tot + arr[cur][i])
        visited[i] = False # 썼으면 돌려놔


T = int(input())

for k in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]

    visited = [False for i in range(n)] # 열 중복 방지를 위한 방문처리배열
    ans = 10000000
    recur(0, n, 0)

    print('#{} {}'.format(k, ans))