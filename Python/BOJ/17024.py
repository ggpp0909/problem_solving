N = int(input())
# 1 <= N <= 100000
arr = [0 for i in range(100100)]
for i in range(N - 1):
    a, b = map(int, input().split())
    arr[a] += 1
    arr[b] += 1

print(max(arr) + 1)
