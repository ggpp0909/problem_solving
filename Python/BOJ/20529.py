import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

T = int(input())

def cal_dis(a, b):
    cnt = 0
    for i in range(4):
        if a[i] != b[i]:
            cnt += 1
    return cnt

def calc(a, b, c):
    return cal_dis(a, b) + cal_dis(b, c) + cal_dis(a, c)

def recur(cur):
    global p, ans

    if cur == 3:
        ans = min(ans, calc(p[0], p[1], p[2]))
        return
    
    for i in range(len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        p.append(arr[i])
        recur(cur + 1)
        p.pop()
        visited[i] = False


for _ in range(T):
    N = int(input())
    arr = input().split()
    if N > 32:
        print(0)
        continue
    visited = [False for i in range(len(arr))]
    p = []
    ans = 99999999999
    recur(0)
    print(ans)