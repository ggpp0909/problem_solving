import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

for k in range(1, n+1):
    eqt = input()
    stack = []

    for i in eqt:
        if i in '+-*/':
            stack.append(i)
        else:
            print(i, end='')
    print(*stack, sep='')
