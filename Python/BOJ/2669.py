rect = [list(map(int, input().split())) for i in range(4)]
arr = [[0 for i in range(100)] for j in range(100)]

for k in rect:
    for i in range(k[1], k[3]):
        for j in range(k[0], k[2]):
            arr[i][j] = 1

tot = 0
for i in arr:
    tot += sum(i)

print(tot)