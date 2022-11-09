def recur(cur, start):
    if cur == M:
        print(*ans)
        return
    
    for i in range(start, N):
        ans[cur] = arr[i]
        recur(cur + 1, i)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = [0 for i in range(M)]
arr.sort()
recur(0, 0)