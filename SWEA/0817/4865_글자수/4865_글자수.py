import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

for k in range(1, n + 1):
    str1 = input()
    str2 = input()

    maxv = 0
    for i in range(len(str1)):
        if maxv < str2.count(str1[i]):
            maxv = str2.count(str1[i])

    print('#{} {}'.format(k, maxv))
