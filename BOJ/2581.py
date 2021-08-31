M = int(input())
N = int(input())

visited = [False for i in range(N + 1)]
arr = []
tot = 0
for i in range(2, N + 1):
    if not visited[i]:
        visited[i] = True
        if i >= M:
            arr.append(i)
            tot += i
    for j in range(i, N + 1, i):
        visited[j] = True

if arr:
    print(tot)
    print(arr[0])
else:
    print(-1)