def recur(cur):
    if cur == M:
        print(*ans)
        return
    
    for i in range(N):
        if visited[i]:
            continue
        
        visited[i] = True
        ans[cur] = arr[i]
        recur(cur + 1)
        visited[i] = False

N, M = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for i in range(N)]
ans = [0 for i in range(M)]
arr.sort()
recur(0)