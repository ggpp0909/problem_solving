N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
ans = 99999999

def recur(cur, tot, cnt, visit):
    global ans

    if ans < tot:
        return

    if cnt == N - 1:
        if arr[cur][0]:
            tot += arr[cur][0]
            ans = min(ans, tot)
        return

    for i in range(N):
        if visit & (1 << i) or arr[cur][i] == 0:
            continue
        recur(i, tot + arr[cur][i], cnt + 1, visit | (1 << i))

recur(0, 0, 0, 1)
print(ans)