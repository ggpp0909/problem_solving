import sys
sys.stdin = open('input.txt')

def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))


def merge(left, right):
    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    result = []
    l = 0
    r = 0
    while len(left) > l or len(right) > r:
        if len(left) > l and len(right) > r:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        elif len(left) > l:
            result.append(left[l])
            l += 1
        elif len(right) > r:
            result.append(right[r])
            r += 1

    return result

T = int(input())

for k in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    cnt = 0
    print('#{} {} {}'.format(k, merge_sort(arr)[len(arr)//2], cnt))





