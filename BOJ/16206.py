N, M = map(int, input().split())
arr = list(map(int, input().split()))
div_10 = [False for i in range(N)]
arr.sort()

cnt = 0
for i in range(N):
    if arr[i] == 10:
        cnt += 1
        div_10[i] = True
        continue

    if M == 0:
        break

    if arr[i] % 10 == 0:
        div_10[i] = True
        temp = arr[i]

        while M > 0 and temp // 10 != 1:
            temp -= 10
            cnt += 1
            M -= 1
        if temp // 10 == 1:
            cnt += 1

if M != 0:
    for i in range(N):
        if M == 0:
            break

        if not div_10[i]:
            temp = arr[i]
            while M > 0 and temp // 10 >= 1:
                temp -= 10
                cnt += 1
                M -= 1

print(cnt)