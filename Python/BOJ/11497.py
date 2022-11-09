T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    arr_1 = []
    arr_2 = []

    for i in range(0, N):
        if i % 2:
            arr_2.append(arr[i])
        else:
            arr_1.append(arr[i])
    arr_2.sort(reverse=True)
    arr_1 += arr_2

    # print(arr_1)
    ans = 0
    for i in range(N - 1, 0, -1): # 끝에서 시작 이유, arr_1[0]과 arr_1[-1] 비교하기위해
        ans = max(ans, abs(arr_1[i] - arr_1[i - 1]))
    print(ans)