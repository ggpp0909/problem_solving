n = int(input())
arr = list(map(int, input().split()))

arr.sort()

s = 0
e = n - 1
ans = 100000000000
while s < e:
    if ans > abs(arr[s] + arr[e]):
        ans = abs(arr[s] + arr[e])
        A = arr[s]
        B = arr[e]

    if arr[s] + arr[e] < 0:
        s += 1
    else:
        e -= 1

print(A, B)
