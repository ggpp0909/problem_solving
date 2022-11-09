import sys
sys.stdin = open('input.txt')

pw = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    arr = [input() for i in range(n)]

    flag = 0
    password = ''
    for i in range(n):
        temp = arr[i][::-1]
        for j in range(m):
            if temp[j] == '1':
                flag = 1
                for k in range(56):
                    password += temp[j + k]
                break
        if flag:
            break

    password = password[::-1]
    pass_to_dec = []
    for i in range(0, 56, 7):
        pass_to_dec.append(pw[password[i:i+7]])

    even = 0
    odd = 0
    for i in range(7):
        if i % 2:
            odd += pass_to_dec[i]
        else:
            even += pass_to_dec[i]
    ans = 0
    if (even * 3 + odd + pass_to_dec[-1]) % 10 == 0:
        ans = sum(pass_to_dec)

    print('#{} {}'.format(_ + 1, ans))