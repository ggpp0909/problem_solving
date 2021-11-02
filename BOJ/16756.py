import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
ans = 100000000000
for i in range(n - 1):
    temp = abs(arr[i] - arr[i + 1])
    if ans > temp:
        ans = temp

print(ans)