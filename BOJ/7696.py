N, K = map(int, input().split())

lst = []
for i in range(1,K+1):
    lst.append(str(N * i)[::-1])

ans = 0
for i in lst:
    if lst[-1] != '0':
        ans = max(ans, int(i))

print(ans)