import sys
input = sys.stdin.readline

T = 1
while True:
    N = int(input())
    if N == 0: break

    arr = [input().split() for i in range(N)]
    par = list(range(N + 1))
    # 무지성 union하고 마지막에 path compression 한번 돌아주면 부모 이름 종류수가 연결고리수

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        par[x] = y

    index_matching = {}
    for i in range(len(arr)):
        index_matching[arr[i][0]] = i

    for i in range(len(arr)):
        if find(index_matching[arr[i][0]]) == find(index_matching[arr[i][1]]):
            continue
        union(index_matching[arr[i][0]], index_matching[arr[i][1]])

    for i in range(len(arr)):
        find(i)

    ans = len(set(par[:-2]))
    # print(par)
    print(T, ans)
    T += 1