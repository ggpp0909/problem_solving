arr = list(range(1, 11))
ans = []

def recur(cur=0, tot=0):
    if tot == 10:
        print(*ans)
        return

    if cur >= 10 or tot > 10:
        return

    ans.append(arr[cur])
    recur(cur + 1, tot + arr[cur])
    ans.pop()
    recur(cur + 1, tot)

recur()