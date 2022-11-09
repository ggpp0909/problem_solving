n = int(input())
arr = [[0 for i in range(100)] for j in range(100)]
for k in range(n):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            arr[i][j] = 1

tot = 0
for i in range(100):
    for j in range(100):
        tot += arr[i][j]

print(tot)