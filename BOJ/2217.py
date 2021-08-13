n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

length = len(arr)
arr.sort()
ans = arr[0]
for i in range(len(arr)):
    ans = max(ans, arr[i]*(length-i))

print(ans)