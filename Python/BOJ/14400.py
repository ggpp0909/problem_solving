n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

cx = x[n//2]
cy = y[n//2]

tot = 0
for i in range(n):
    tot += abs(cx-x[i]) + abs(cy-y[i])

print(tot)

