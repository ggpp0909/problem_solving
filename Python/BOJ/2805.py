import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

s = 0
e = 1000000000
ans = 0
while s <= e:
    mid = (s + e) // 2
    tot = 0
    for i in arr:
        tot += max(0, i - mid)

    if tot >= M:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)