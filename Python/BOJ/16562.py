N, M, k = map(int, input().split()) # 학생수, 친구관계수, 가진 돈
arr = [0] + list(map(int, input().split()))

par = list(range(N + 1))

def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

# def union(x, y):
#     x = find(x)
#     y = find(y)
#     par[x] = y

for i in range(M):
    a, b = map(int, input().split())
    a = find(a) # 루트의 비용을 비교해야 하므로
    b = find(b)
    if arr[a] > arr[b]: # a의 비용이 더 비싸면 b를 부모로
        par[a] = b
    else:
        par[b] = a
# print(par)
for i in range(1, N + 1):
    find(i)

newpar = set(par[1:])
# print(visited)
# print(newpar)
ans = 0
for i in newpar:
    ans += arr[i]

# print(visited)
if ans <= k:
    print(ans)
else:
    print("Oh no")