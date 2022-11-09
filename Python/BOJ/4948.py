visited = [False for i in range(250000)]
arr = []
for i in range(2, 250000):
    if not visited[i]:
        visited[i] = True     
        arr.append(i)
    for j in range(i, 250000, i):
        visited[j] = True

while True:
    N = int(input())
    if N == 0:
        break
    cnt = 0
    for i in arr:
        if i > 2 * N:
            break
        if N < i:
            cnt += 1
    
    print(cnt)
