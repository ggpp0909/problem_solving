N = int(input())
M = int(input())

v = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

visited[1] = True

cnt = 0
def recur(cur = 1):
    global cnt

    for i in v[cur]:
        if visited[i]:
            continue
        visited[i] = True
        cnt += 1
        recur(i)

recur()
print(cnt)