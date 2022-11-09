# 1 2 3 4 5 6 7
# 3 3 3 3 3
#   2 2 2 2
#     4 4 4
#       4 4
#         8
# 


T = int(input())

visited = [[False for i in range(1001)] for j in range(1001)]
visited[1][1] = True

ans = [0 for i in range(1001)]
ans[1] = 3
def gcd(x, y):
    while x % y != 0:
        x, y = y, x % y

    return y

for i in range(2, 1001): # 세로
    temp = 0
    for j in range(1, i + 1): # 가로
        GCD = gcd(i, j)
        son = i // GCD
        mom = j // GCD
        if visited[son][mom]:
            continue
        visited[son][mom] = True
        temp += 1
    ans[i] = ans[i - 1] + temp * 2

# print(ans)
for _ in range(T):
    print(ans[int(input())])