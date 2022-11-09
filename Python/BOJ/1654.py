K, N = map(int, input().split())
arr = [int(input()) for i in range(K)]

s = 0
e = 10000000000
ans = 0
while s <= e:
    mid = (s + e) // 2
    tot = 0
    for i in range(len(arr)):
        tot += arr[i] // mid

    if tot >= N:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
print(ans)