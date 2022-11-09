N = int(input())
arr = list(map(int, input().split()))
visited = [False for i in range(N + 10)]
ans = 0

def recur(cur = 0, tot = 0, prev = 0):
    global ans
    if cur == len(arr) - 1:
        if ans < tot:
            ans = tot
        return

    visited[prev] = True
    for i in range(len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        temp = abs(arr[prev] - arr[i])
        recur(cur + 1, tot + temp, i)
        visited[i] = False
    visited[prev] = False

for i in range(len(arr)):
    recur(0,0,i)
print(ans)