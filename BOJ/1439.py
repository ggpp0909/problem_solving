a = input()
cnt = 0

for i in range(len(a)):
    if a[i-1] != a[i]:
        cnt += 1

if cnt % 2 == 0:
    print(cnt//2)
else:
    print(cnt//2 + 1)