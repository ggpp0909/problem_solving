n = int(input())
a = int(input())

arr = [0 for i in range(1010)]
idx = 0
for i in range(n-1):
    opp = int(input())
    arr[opp] += 1
    if idx < opp:
        idx = opp

cnt = 0
while True:
    if a > idx:
        print(cnt)
        break

    a += 1
    cnt += 1
    arr[idx] -= 1
    arr[idx - 1] += 1
    if arr[idx] == 0:
        idx -= 1