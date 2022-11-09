import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

for k in range(1, n+1):
    word = list(input())
    arr = []
    cnt = 0
    ans = len(word)

    for i in range(len(word)):
        if len(arr) == 0 or arr[-1] != word[i]:
            arr.append(word[i])
        else:
            arr.pop()

    print('#{} {}'.format(k, len(arr)))


