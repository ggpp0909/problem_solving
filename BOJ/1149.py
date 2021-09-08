n = int(input())
arr =[[0, 0, 0]] + [list(map(int, input().split())) for i in range(n)]

dp_R = [0 for i in range(n + 1)]
dp_G = [0 for i in range(n + 1)]
dp_B = [0 for i in range(n + 1)]

for i in range(1, len(arr)):
    dp_R[i] = arr[i][0] + min(dp_G[i - 1], dp_B[i - 1])
    dp_G[i] = arr[i][1] + min(dp_R[i - 1], dp_B[i - 1])
    dp_B[i] = arr[i][2] + min(dp_R[i - 1], dp_G[i - 1])

print(min(dp_R[n], dp_G[n], dp_B[n]))