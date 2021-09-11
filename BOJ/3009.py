arr = [list(map(int, input().split())) for i in range(3)]

x = [0 for i in range(1001)]
y = [0 for i in range(1001)]

for i in arr:
    x[i[0]] += 1
    y[i[1]] += 1

for i in range(len(x)):
    if x[i] == 1:
        print(i, end=' ')
for i in range(len(y)):
    if y[i] == 1:
        print(i)


