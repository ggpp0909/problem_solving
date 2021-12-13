import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

query = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(K)]

for i in range(K):
    L, R, X = query[i]
    for i in range(L - 1, R):
        arr[i] += X

    arr.sort()

print(*arr)

