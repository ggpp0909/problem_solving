import sys

N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()

idx = len(arr) - 1
while idx >= 2:
    if arr[idx] < arr[idx - 1] + arr[idx - 2]:
        print(arr[idx] + arr[idx - 1] + arr[idx - 2])
        break
    else:
        idx -= 1
else:
    print(-1)