n, m = map(int, input().split())
arr = [int(input()) for i in range(n)]
arr.sort()

def check(x):
    cnt = 1
    prv = arr[0]

    for i in range(1, n):
        if arr[i] >= prv + x:
            cnt += 1
            prv = arr[i]

    return cnt >= m

s = 1
e = 1000000000
ans = 0
#최대값을 구하고싶다 [t,t,T,f,f ...]
while s <= e:
    mid = (s + e) // 2  # 공유기 사이의 거리가 mid,

    if check(mid):  # mid간격으로 설치했을 때 m개이상 설치가 되나?
        ans = mid
        s = mid + 1     #되면 s를 땡겨: 더나은값(더 최대가 있는지 찾아야해)
    else:
        e = mid - 1     #안되면 e를 땡겨

print(ans)