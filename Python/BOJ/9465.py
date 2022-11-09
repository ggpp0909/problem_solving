tc = int(input())

for _ in range(tc):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    dp1 = [0 for i in range(n + 1)]
    dp2 = [0 for i in range(n + 1)]

    dp1[1] = arr1[0]
    dp2[1] = arr2[0]

    for i in range(2, n + 1):
        dp1[i] = arr1[i - 1] + max(dp2[i - 1], dp2[i - 2])
        dp2[i] = arr2[i - 1] + max(dp1[i - 1], dp1[i - 2])

    print(max(dp1[-1], dp2[-1]))