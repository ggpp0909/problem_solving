def chik_dis(a, b):
    val = abs(a[0]-b[0]) + abs(a[1]-b[1])
    return val

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
chik = []
home = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chik.append([i, j])
        if arr[i][j] == 1:
            home.append([i, j])

pick = []
ans = 1000000
def recur(cur, cnt):
    global ans

    if cnt == M:
        temp = 0
        for i in range(len(home)):
            tot = 1000
            for j in range(len(pick)):
                 tot = min(tot, chik_dis(pick[j], home[i]))
            temp += tot
        ans = min(ans,temp)
        return

    if cur == len(chik):
        return

    pick.append(chik[cur])
    recur(cur + 1, cnt + 1)
    pick.pop()
    recur(cur + 1, cnt)

recur(0,0)

print(ans)


