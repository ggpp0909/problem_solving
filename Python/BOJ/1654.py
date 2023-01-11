K, N = map(int, input().split())
arr = [int(input()) for i in range(K)]

s = 0
e = 10000000000
ans = 0

# 매개변수 탐색
while s <= e:
    mid = (s + e) // 2

    tot = 0
    for i in range(len(arr)):
        tot += arr[i] // mid

    if tot >= N: # 만족 하면?
        ans = mid # 일단 답에 넣어
        s = mid + 1 # 더 나은 답이 있는지 더 찾아보는거
    else: # 만족 못하면
        e = mid - 1 # 되돌아가

print(ans)

