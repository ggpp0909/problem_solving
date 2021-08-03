n, m = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

cnt = 0
for i in coin[::-1]:
    if i > m:
        continue

    while m >= i :
        m -= i
        cnt += 1
    
print(cnt)