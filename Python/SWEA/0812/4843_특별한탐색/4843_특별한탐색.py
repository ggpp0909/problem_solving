import sys
sys.stdin = open('input.txt')

n = int(input())
for k in range(1, n+1):
    a = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(a):
        temp_idx = i
        for j in range(i, a):
            if i % 2: # 1번인덱스부터
                if arr[j] < arr[temp_idx]:
                    temp_idx = j
            else:
                if arr[j] > arr[temp_idx]:
                    temp_idx = j

        arr[i], arr[temp_idx] = arr[temp_idx], arr[i]

    print('#{}'.format(k), end=' ')
    print(*arr[:10])