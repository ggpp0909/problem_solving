alpha = 'abcdefghijklmnopqrstuvwxyz'

a = input()
ans = [0] * 26
for i in a:
    ans[alpha.index(i)] += 1

print(*ans)
