N, M = map(int, input().split())
b = [0] * 7
g = [0] * 7

for i in range(N):
    s, y = map(int, input().split())
    if s == 1:
        b[y] += 1
    elif s == 0:
        g[y] += 1

ans = 0
for i in range(1,7):
    ans += (b[i]+(M-1)) // M + (g[i]+(M-1)) // M

print(ans)
