n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr.sort()

for i in arr2:
    s = 0
    e = n - 1
    while s <= e:
        mid = (s + e) // 2
        if i == arr[mid]:
            print(1)
            break
        elif i > arr[mid]:
            s = mid + 1
        else:
            e = mid - 1
    else:
        print(0)
