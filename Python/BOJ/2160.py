T = int(input())

arr = [[input() for i in range(5)] for j in range(T)]

def check(A, B):
    global temp
    cnt = 0
    for i in range(5):
        for j in range(7):
            if A[i][j] != B[i][j]:
                cnt += 1
                if cnt >= temp:
                    return 99999999
    return cnt

ans = []
temp = 999999
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        now = check(arr[i], arr[j])
        if temp > now:
            ans = [i + 1, j + 1]
            temp = now

print(*ans)
