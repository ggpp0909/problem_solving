n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

s = 0
e = len(arr) - 1
cnt = 0

while s < e:
    temp = arr[s] + arr[e]
    if x == temp:
        cnt += 1
        s += 1
        e -= 1
    elif x > temp:
        s += 1
    else:
        e -= 1

print(cnt)