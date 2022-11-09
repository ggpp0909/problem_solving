N, k = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = k - 1
ans = tot = sum(arr[s:e + 1])

while e <= len(arr) - 2:
    e += 1
    tot = tot + arr[e] - arr[s]
    s += 1
    ans = max(ans, tot)

print(ans)