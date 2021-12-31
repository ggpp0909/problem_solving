N, K, B = map(int, input().split())
arr = [0 for i in range(N + 1)]

for i in range(B):
    arr[int(input())] = 1

s = 1
e = K
tot = sum(arr[s:e + 1])
ans = tot
while e < N:
    tot -= arr[s]
    s += 1

    e += 1
    tot += arr[e]

    ans = min(ans, tot)

print(ans)