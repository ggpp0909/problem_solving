N, M = map(int, input().split())
arr = list(map(int, input().split()))

neg = []
pos = []
for i in arr:
    if i < 0:
        neg.append(-1 * i)
    if i > 0:
        pos.append(i)

neg.sort()
pos.sort()

tot = 0
for i in range(len(neg) - 1, -1, -M):
    tot += 2 * neg[i]
for i in range(len(pos) - 1, -1, -M):
    tot += 2 * pos[i]

if neg and pos:
    last = max(neg[-1], pos[-1])
elif neg:
    last = neg[-1]
else:
    last = pos[-1]

print(tot - last)
