import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

for k in range(1, n+1):
    word = list(input())
    arr = []
    ans = 1
    for i in range(len(word)):
        if word[i] == '(' or word[i] == '{':
            arr.append(word[i])
        elif word[i] == ')' or word[i] == '}':
            if len(arr) == 0:
                ans = 0
                break
            elif word[i] == ')' and arr.pop() != '(':
                ans = 0
                break
            elif word[i] == '}' and arr.pop() != '{':
                ans = 0
                break

    if len(arr) != 0:
        ans = 0

    print('#{} {}'.format(k, ans))
