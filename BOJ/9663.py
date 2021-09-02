n = int(input())
visited = [False for i in range(n)]
visited2 = [False for i in range(3 * n)] #/
visited3 = [False for i in range(3 * n)] #\

cnt = 0
def recur(cur=0):
    global cnt

    if cur == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i] or visited2[cur + i] or visited3[n + cur - i]:
            continue

        visited[i] = True
        visited2[cur + i] = True
        visited3[n + cur - i] = True
        recur(cur + 1)
        visited[i] = False
        visited2[cur + i] = False
        visited3[n + cur - i] = False

recur()
print(cnt)