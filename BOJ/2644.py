n = int(input())

start, end = map(int, input().split())

v = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]

n2 = int(input())

for i in range(n2):
    temp1, temp2 = map(int, input().split())
    v[temp1].append(temp2)
    v[temp2].append(temp1)

ans = -1

def dfs(n, cnt=0):
    global end, ans

    if n == end:
        ans = cnt

    for i in v[n]:
        if visited[i] == True:
            continue
        visited[i] = True
        dfs(i, cnt + 1)
        visited[i] = False

dfs(start, 0)
print(ans)