import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

for k in range(1, n+1):
    razer = input().replace('()', '1')

    cnt = 0  # 몇 겹이 겹쳐져있냐
    ans = 0
    for i in razer:
        if i == '(':
            cnt += 1
        if i == '1':
            ans += cnt
        if i == ')':
            ans += 1
            cnt -= 1

    print('#{} {}'.format(k, ans))

