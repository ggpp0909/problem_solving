import sys

M = int(sys.stdin.readline().rstrip())

S = 0
# 처음생각 append pop -> 시간초과
# 리스트? 가능, -> 비트마스킹 (메모리, 시간 이득)

for _ in range(M):
    i = sys.stdin.readline().rstrip().split(' ')

    if i[0] == 'add':
        S |= (1 << int(i[1]))

    elif i[0] == 'check':
        if S & (1 << int(i[1])):
            print(1)
        else:
            print(0)

    elif i[0] == 'remove':
        S &= (~(1 << int(i[1])))

    elif i[0] == 'toggle':
        S ^= (1 << int(i[1]))

    elif i[0] == 'empty':
        S = 0

    elif i[0] == 'all':
        S = (1 << 21) - 1 # 우선순위 이슈