tc = int(input())
for _ in range(tc):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()
    ans = 0
    for i in range(len(A)):
        temp = A[i]
        s = 0
        e = len(B) - 1
        while s <= e:
            mid = (s + e) // 2
            if B[mid] < temp:
                cnt = mid
                s = mid + 1
            else:
                e = mid - 1
        ans += s
    print(ans)