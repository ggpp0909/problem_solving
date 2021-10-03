import sys
sys.stdin = open('input.txt', encoding='UTF8')

for k in range(1, 11):
    word = input().split()
    arr = []
    cnt = 0

    for i in range(int(word[0])):
        if len(arr) == 0 or arr[-1] != word[1][i]:
            arr.append(word[1][i])
        else:
            arr.pop()

    print('#{}'.format(k),end=' ')
    print(*arr, sep='')