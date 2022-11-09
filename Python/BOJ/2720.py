n = int(input())
arr = [25,10,5,1]
for i in range(n):
    money = int(input())
    change = 0

    ans = []
    for j in arr:
        change = money//j
        money %= j
        ans.append(change)

    print(*ans)
    