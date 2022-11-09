arr = list(range(1, 11))
sub = []
def recur(cur = 0, tot = 0):
    if tot == 10:
        print(*sub)
        return

    # 가지치기, 합이 10이 넘거나 cur이 최대를 넘는 node는 유망성이 없으므로 후퇴
    if tot > 10 or cur == len(arr):
        return

    sub.append(arr[cur])
    recur(cur + 1, tot + arr[cur])
    sub.pop()
    recur(cur + 1, tot)

recur()
