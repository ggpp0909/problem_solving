import sys
sys.stdin = open('input.txt')

def recur(cur, n, tot):
    global ans

    if cur == n: # 기저 왔으면 갱신해
        ans = max(ans, tot)
        return

    if tot <= ans: # 1보다 작은수들끼리는 곱할수록 작아지므로 가지치기 가능
        return

    for i in range(n):
        if visited[i]: # 쓴 열은 쓰지마
            continue
        visited[i] = True # 이거 쓸거야
        recur(cur + 1, n, tot * arr[cur][i] * 0.01)
        visited[i] = False # 썼으면 돌려놔

T = int(input())

for k in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]

    visited = [False for i in range(n)] # 열 중복 방지를 위한 방문처리배열
    ans = 0
    recur(0, n, 1)

    print('#{} {:.6f}'.format(k, ans * 100))