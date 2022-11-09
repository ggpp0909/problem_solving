import sys
sys.stdin = open('input.txt')

n = int(input())

for k in range(1,n + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    minv = maxv = arr[0]
    for i in range(N):
        if minv > arr[i]:
            minv = arr[i]
        if maxv < arr[i]:
            maxv = arr[i]

    result = maxv - minv
    print('#{} {}'.format(k, result))