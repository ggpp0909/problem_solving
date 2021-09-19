n = int(input())
cnt2 = 0
cnt5 = 0
for i in range(1, n + 1):
    temp = i
    while temp % 2 == 0:
        temp //= 2
        cnt2 += 1
    temp = i
    while temp % 5 == 0:
        temp //= 5
        cnt5 += 1

print(min(cnt2, cnt5))