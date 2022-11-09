import sys

N = int(input())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))


arr1.sort()


def binary_search(num):
    s = 0
    e = len(arr1) - 1

    while s <= e:
        mid = (s + e) // 2

        if arr1[mid] == num:
            return 1

        elif arr1[mid] > num:
            e = mid - 1

        else:
            s = mid + 1

    return 0


for i in arr2:
    print(binary_search(i), end=" ")
