k = int(input())
arr = input().split()
visited = [False for i in range(10)]
ans_min = '9999999999'
ans_max = '0'
def recur(cur=0, ans='', pre=0):
    global k, ans_min, ans_max
    if cur == len(arr):
        if int(str(k) + ans) < int(ans_min):
            ans_min = str(k) + ans
        if int(str(k) + ans) > int(ans_max):
            ans_max = str(k) + ans
        return

    for i in range(10):
        if visited[i]:
            continue
        visited[i] = True
        if arr[cur] == '<':
            if i > pre:
                recur(cur + 1, ans + str(i), i)
        elif arr[cur] == '>':
            if i < pre:
                recur(cur + 1, ans + str(i), i)
        visited[i] = False

for i in range(10):
    k = i
    visited[i] = True
    recur(cur=0, ans='', pre=i)
    visited[i] = False

print(ans_max)
print(ans_min)