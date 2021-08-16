def recur(cur = 0, start = 0):
    if cur == 6:
        print(*ans)
        return

    for i in range(start, len(arr)):
        ans.append(arr[i])
        recur(cur + 1, i + 1)
        ans.pop()

while True:
    ans = []
    a = list(map(int, input().split()))
    if a[0] == 0:
        exit()
    arr = sorted(a[1:])
    recur()
    print('')