N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
def recur(cur = 0, tot = 0, cnt = 0):
    global ans

    #가지치기
    if tot > M:
        return

    if cnt == 3:
        if ans < tot:
            ans = tot
        return
    
    if cur == N:
        return

    recur(cur + 1, tot+arr[cur], cnt + 1)
    recur(cur + 1, tot, cnt)

recur()
print(ans)