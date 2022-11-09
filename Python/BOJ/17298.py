n = int(input())
arr = [10000000] + list(map(int, input().split()))[::-1]

stack = []
stack.append(0)
ans = []
for i in range(1, len(arr)):
    while arr[i] >= arr[stack[-1]]:
        stack.pop()
    if stack[-1] == 0:
        ans.append(-1)
    else:
        ans.append(arr[stack[-1]])
    stack.append(i)

print(*ans[::-1])