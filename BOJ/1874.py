n = int(input())
stack = []
ans = [int(input()) for i in range(n)]
idx = 0
annns = []

for j in range(1, n+1):
    stack.append(j)
    annns.append('+')
    if stack and stack[-1] == ans[idx]:
        while stack and idx < n and stack[-1] == ans[idx]:
            stack.pop()
            idx += 1
            annns.append('-')
if annns.count('+') == annns.count('-'):
    for i in annns:
        print(i)
else:
    print('NO')


