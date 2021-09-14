import sys

n = int(input())
arr = [-1] + list(map(int, sys.stdin.readline().split()))

l_width = [0 for i in range(n + 1)]
r_width = [0 for i in range(n + 1)]

stack = []
stack.append(0)
for i in range(1, n + 1):
    while arr[i] <= arr[stack[-1]]:
        stack.pop()
    l_width[i] = stack[-1]
    stack.append(i)

arr2 = [-1] + arr[::-1]
stack = []
stack.append(0)
for i in range(1, n + 1):
    while arr2[i] <= arr2[stack[-1]]:
        stack.pop()
    r_width[i] = stack[-1]
    stack.append(i)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, arr[i] * (n - r_width[n - i + 1] - l_width[i]))
print(ans)
