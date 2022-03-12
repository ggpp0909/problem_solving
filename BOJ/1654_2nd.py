K, N = map(int, input().split())

arr = [int(input()) for i in range(K)]

s = 0
e = 2 ** 31
ans = 0
while s <= e:
    mid = (s + e) // 2
    #랜선을 잘라서 모두 mid길이만큼 만들었을때 나올수 있는 값

    temp = 0
    for i in arr:
        temp += i // mid

    # 최대 길이를 찾아야 함
    if temp >= N: # N개를 만들 수 있으면 더 나은 값이 있는지 찾아야함
        ans = mid
        s = mid + 1
    else:# N개를 만들 수 없으니 mid 길이를 더 줄여서 N개 이상으로 만들어야됨
        e = mid - 1

print(ans)