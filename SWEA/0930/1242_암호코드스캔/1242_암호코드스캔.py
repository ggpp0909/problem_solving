import sys
sys.stdin = open('input.txt')

T = int(input())

htob = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'
}

ratio = { # 암호코드는 0101의 비율로 이루어져있다. 101의 비율로 코드해독하기위한 딕셔너리
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9,
}

for k in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]

    arr = list(set(arr))
    N2 = len(arr)

    temp = [''] * N2
    for i in range(N2):
        for j in range(M):
            temp[i] += htob[arr[i][j]] # 각 숫자 2진수로 바꿔서 저장

    ans = 0
    visited = []
    for password in temp:
        decode = []
        # 암호 비율
        a = b = c = d = 0
        length = len(password)
        for i in range(length - 1, -1, -1):
            if c == 0 and password[i] == '1': # 처음 1을 만났을때 d의 개수 증가
                d += 1
            elif d > 0 and b == 0 and password[i] == '0': # 그다음 0 찾으면
                c += 1
            elif a == 0 and c > 0 and password[i] == '1':
                b += 1
            elif b > 0 and password[i] == '0': # 뒤에서부터 1 0 1 찾고 그다음 0일때 코드 해독
                temp = min(b, c, d) # 비율 일치 시키기
                b //= temp
                c //= temp
                d //= temp
                key = str(b) + str(c) + str(d)
                decode = [ratio[key]] + decode
                a = b = c = d = 0

                if len(decode) == 8:
                    if decode not in visited:
                        visited.append(decode)
                        even = 0
                        odd = 0
                        for j in range(7):
                            if j % 2:
                                odd += decode[j]
                            else:
                                even += decode[j]
                        if (even * 3 + odd + decode[-1]) % 10 == 0:
                            ans += sum(decode)
                    decode = []

    print('#{} {}'.format(k, ans))

