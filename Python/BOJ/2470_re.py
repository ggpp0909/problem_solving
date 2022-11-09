import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

s = 0
e = N - 1
ans = 9999999999

while s < e:
    if abs(arr[s] + arr[e]) < ans:
        ans = abs(arr[s] + arr[e])
        A = arr[s]
        B = arr[e]

    if arr[s] + arr[e] < 0:
        s += 1
    else:
        e -= 1

print(A, B)
