m, n = map(int, input().split())
arr = [0] * 1010
visited = [False] * (m + 1)


def recur(cur):
    if cur == n:
        for k in range(n):
            print(arr[k], end=" ")
        print("")

        return

    for i in range(1, m + 1):
        if visited[i]:
            continue

        visited[i] = True
        arr[cur] = i
        recur(cur + 1)
        visited[i] = False


recur(0)
