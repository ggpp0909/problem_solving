import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

for k in range(1, n+1):
    N = int(input())
    room = [list(map(int, input().split())) for i in range(N)]

    for i in room:
        for j in range(len(i)):
            i[j] = (i[j] + 1) // 2

    arr = [0] * 1000
    for i in room:
        if i[0] <= i[1]:
            for j in range(i[0], i[1]+1):
                arr[j] += 1
        else:  # 반례 -> 거꾸로 갈경우 range범위 수정 
            for j in range(i[0], i[1]-1, -1):
                arr[j] += 1
    print('#{} {}'.format(k, max(arr)))

