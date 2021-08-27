n = int(input())
maxv = 0
tot = 0
for i in range(n):
    temp = int(input())
    maxv = max(temp, maxv)
    tot += temp
other = tot - maxv

if maxv >= other:
    print(maxv - other)
else:
    if tot % 2:
        print(1)
    else:
        print(0)
