import sys
sys.stdin = open('input.txt')

n = int(input())
for k in range(1, n + 1):
    leng = int(input())
    arr = [list(map(int, input().split())) for i in range(leng)]
    visited = [False for i in range(leng)]
    ans = 999999

    def recur(cur=0, tot=0):
        global ans
        if cur == leng:
            ans = min(ans, tot)
            return

        if tot > ans:
            return

        for i in range(leng):
            if visited[i]:
                continue
            visited[i] = True
            recur(cur + 1, tot + arr[cur][i])
            visited[i] = False

    recur()
    print('#{} {}'.format(k, ans))
