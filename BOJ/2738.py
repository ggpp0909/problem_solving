N, M = map(int, input().split())
arr = []
for i in range(2 * N):
    temp = list(map(int, input().split()))
    arr.append(temp)

ans = []

for i in range(N):
    temp_arr = []
    for j in range(M):
        temp = arr[i][j] + arr[i + N][j]
        temp_arr.append(temp)
    ans.append(temp_arr)

# print(ans)

for i in ans:
    print(*i)