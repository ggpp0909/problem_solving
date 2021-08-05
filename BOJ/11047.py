n, m = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

cnt = 0
for i in coin[::-1]:
    if m >= i:
        cnt += m // i
        m %= i
    
print(cnt)