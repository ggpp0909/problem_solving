def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

def union(x, y):
    x = find(x)
    y = find(y)

    par[x] = y


def is_MST():
    for i in range(N + 1):
        find(i)
    if len(set(par[1:])) == 1:
        return True
    else:
        return False

N, M, K = map(int, input().split())
temp = [list(map(int, input().split())) + [i] for i in range(1, M + 1)]
visited = [False for i in range(M)]

ans_arr = []
for k in range(K):
    par = list(range(N + 1))

    ans = 0
    for i in range(len(temp)):
        if find(temp[i][0]) == find(temp[i][1]) or visited[i]:
            continue
        union(temp[i][0], temp[i][1])
        ans += temp[i][2]

    visited[k] = True

    if is_MST():
        ans_arr.append(ans)
    else:
        ans_arr.append(0)

print(*ans_arr)
