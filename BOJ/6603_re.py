def recur(cur=0, start=0):
    if cur == 6:
        print(*ans)
        return

    for i in range(start, len(arr)):
        ans.append(arr[i])
        recur(cur + 1, i + 1)
        ans.pop()


while True:
    ans = []
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        exit()
    arr = arr[1:]
    recur()
    print()
