n = int(input())
arr = list(map(int, input().split()))
x = int(input())
v = [[] for i in range(n)]

for i in range(n):
    if arr[i] == -1:
        root = i
    elif arr[i] == x or i == x:
        continue
    else:
        v[arr[i]].append(i)

cnt = 0
def recur(cur):
    global cnt
    if v[cur]:
        for i in v[cur]:
            recur(i)
    else:
        cnt += 1

if root == x:
    print(0)
else:
    recur(root)
    print(cnt)