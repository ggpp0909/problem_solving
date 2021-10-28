T = int(input().rstrip())

def bs(s, e, temp):
    while s <= e:
        mid = (s + e) // 2
        if temp > arr1[mid]:
            s = mid + 1
        elif temp < arr1[mid]:
            e = mid - 1
        else:
            print(1)
            return
    else:
        print(0)
        return

for _ in range(T):
    N = int(input())
    arr1 = list(map(int, input().split()))
    M = int(input())
    arr2 = list(map(int, input().split()))

    arr1.sort()
    for i in range(M):
        s = 0
        e = N - 1
        bs(s, e, arr2[i])