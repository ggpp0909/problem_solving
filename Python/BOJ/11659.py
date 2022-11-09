import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
prefix = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + arr[i]

for k in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(prefix[j] - prefix[i - 1])