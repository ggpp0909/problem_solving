import sys
sys.stdin = open('input.txt')

def itoa(num):
    ans = ''
    is_neg = ''
    if num < 0:
        is_neg = '-'

    num = abs(num)
    while num > 0:
        temp = num % 10
        ans += chr(48 + temp)
        num //= 10
    ans += is_neg  # 음수일때만 '-'

    return ans[::-1]  # 앞에서부터 쌓았으므로 거꾸로 리턴

n = int(input())

for k in range(1, n+1):
    num = int(input())
    print('#{} {} {}'.format(k, itoa(num), type(itoa(num))))
