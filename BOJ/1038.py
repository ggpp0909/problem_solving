n = int(input())
if n == 0:
   print(0)
   exit()
ans = -1
cnt = 0
def recur(cur, number, start):
    global cnt, len, ans
    if number > 9876543210:
        print(-1)
        exit()
    if cur == len:
        cnt += 1
        if cnt == n:
            ans = number
        return

    for i in range(start + 1):
        if cur == 0 and i == 0:
            continue

        recur(cur + 1, number * 10 + i, i - 1)

for len in range(1, 100):
    recur(0, 0, 9)

    if cnt >= n:
        break
print(ans)