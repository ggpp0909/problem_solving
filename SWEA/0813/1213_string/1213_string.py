import sys
sys.stdin = open('input.txt', encoding='UTF8')

for k in range(10):
    n = int(input())
    p = input()
    t = input()

    ans = 0
    i = 0
    j = 0
    while i < len(t) and j < len(p):
        if p[j] != t[i]: # 일치하지 않으면 j = 0 i는 처음 인덱스 + 1 로이동
            i = i -j
            j = -1
        i += 1
        j += 1
        if j == len(p): # 모두 일치 -> 카운트 증가, j,i 초기화
            ans += 1
            j = 0

    print('#{} {}'.format(n, ans))

