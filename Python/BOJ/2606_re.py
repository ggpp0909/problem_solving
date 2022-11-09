com = int(input())
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
v = [[] for i in range(com + 1)]
visited = [False for i in range(com + 1)]

# 인접 리스트 만들기
for i in arr:
    v[i[0]].append(i[1])
    v[i[1]].append(i[0])

ans = 0


def recur(cur=1):
    global ans

    for i in v[cur]:
        if visited[i]:
            continue
        visited[i] = True
        ans += 1
        recur(i)


visited[1] = True
recur()
print(ans)
