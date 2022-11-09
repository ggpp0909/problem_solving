import sys
# 투포인터 풀이
N = int(sys.stdin.readline().rstrip())
arr = [-100000000] + list(map(int, sys.stdin.readline().rstrip().split())) + [100000000]
M = int(sys.stdin.readline().rstrip())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

arr3 = []
for i in range(len(arr2)):
    arr3.append([arr2[i], i])
arr3.sort()

ans = [-1 for i in range(500001)]
s = e = 0
for i in range(len(arr3)):
    x = arr3[i][0]

    while arr[s] < x:
        s += 1
    while arr[e] <= x:
        e += 1

    ans[arr3[i][1]] = e - s

for i in range(len(ans)):
    if ans[i] != -1:
        print(ans[i], end=' ')


