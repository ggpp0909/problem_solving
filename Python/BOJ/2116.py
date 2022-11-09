import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
next = [5, 3, 4, 1, 2, 0]
ans = 0

def recur(cur = 0, pair = 0, tot = 0):
    global ans
    if cur == n:
        ans = max(ans, tot)
        return
    
    idx = arr[cur].index(pair)
    max_val = 0
    for i in range(6,0,-1):
        if i != arr[cur][idx] and i != arr[cur][next[idx]]:
            max_val = i
            break
    
    recur(cur + 1, arr[cur][next[idx]], tot + max_val)

for i in range(1, 7):
    recur(pair=i)

print(ans)
