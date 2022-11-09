N, M = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 1
cnt = 0

while e <= N and s <= e:
    total = sum(arr[s:e])
    if total == M:
        cnt += 1
        e += 1
    elif total < M:
        e += 1
    else:
        s += 1

print(cnt)