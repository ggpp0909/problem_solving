import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

for k in range(1, n+1):
    par = list(input())
    arr = []
    ans = 1
    for i in range(len(par)):
        if par[i] == '(':
            arr.append(par[i])
        elif par[i] == ')':
            if len(arr) == 0 or arr.pop() != '(':  # or 순서 중요
                ans = -1
                break

    if len(arr) != 0:
        ans = -1

    print('#{} {}'.format(k, ans))


