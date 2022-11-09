import sys

N, S = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

s = e = 0
tot = arr[0]
ans = 99999999
cnt = 1
while True:
    if tot >= S: # 조건만족
        ans = min(ans, cnt)
        tot -= arr[s]
        s += 1
        cnt -= 1
    elif e == N or s == N:
        break
    else:
        if e != N - 1:
            e += 1
            tot += arr[e]
            cnt += 1
        else:
            tot -= arr[s]
            s += 1
            cnt -= 1

if ans == 99999999:
    ans = 0
print(ans)
