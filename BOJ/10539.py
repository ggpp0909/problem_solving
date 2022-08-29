N = int(input())
arr = list(map(int, input().split()))

ans = []
t = 0
for i in range(N):
    temp = (i + 1) * arr[i] - t
    ans.append(temp)
    t += temp

print(*ans)