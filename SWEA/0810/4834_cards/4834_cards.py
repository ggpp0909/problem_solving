import sys
sys.stdin = open('input.txt')

n = int(input())

for k in range(1, n+1):
    N = int(input())
    cards = list(map(int, input()))

    arr = [0 for i in range(N + 10)]

    for i in range(len(cards)):
        arr[cards[i]] += 1

    mostfreq = arr[0]
    idx = 0
    for i in range(len(arr)):
        if arr[i] >= mostfreq:   # 장수 같아도 업데이트 하도록 > 대신 >=
            mostfreq = arr[i]
            idx = i

    print('#{} {} {}'.format(k, idx, mostfreq))
