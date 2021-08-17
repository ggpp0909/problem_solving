def recur(cur = 0, start = 1):
    if cur == m:
        print(*arr)
        return
    
    for i in range(start, n+1):
        arr[cur] = i
        recur(cur + 1, i)

n, m = map(int, input().split())
arr = [0 for i in range(m)]
recur()