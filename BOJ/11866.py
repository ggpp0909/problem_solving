N, K = map(int, input().split())

q = list(range(1, N + 1))

ans = []
idx = K - 1
while True:
    ans.append(q.pop(idx))
    if len(q) == 0:
        break
    idx = (idx + K - 1) % len(q)

print('<', end='')
print(*ans, sep=', ', end='')
print('>')