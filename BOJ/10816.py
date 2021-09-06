import sys

N = int(sys.stdin.readline().rstrip())
arr = [-100000000] + list(map(int, sys.stdin.readline().rstrip().split())) + [100000000]
M = int(sys.stdin.readline().rstrip())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

for i in range(len(arr2)):
    s = 0
    e = len(arr) - 1

    ans_l = 0
    # 제일 왼쪽 찾기
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] >= arr2[i]:
            ans_l = mid
            e = mid - 1
        else:
            s = mid + 1

    s = 0
    e = len(arr) - 1
    ans_r = 0
    # 제일 오른쪽 찾기
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] > arr2[i]:
            ans_r = mid
            e = mid - 1
        else:
            s = mid + 1

    print(ans_r - ans_l, end=' ')
