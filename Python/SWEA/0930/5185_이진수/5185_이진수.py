import sys
sys.stdin = open('input.txt')

asc = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
]

def aToh(x):
    if x <= '9':
        return ord(x) - ord('0')
    else:
        return ord(x) - ord('0') - 7

def makeT(x):
    global tmp
    for i in range(4):
        tmp += str(asc[x][i])

tc = int(input())
for k in range(tc):
    n, arr = input().split()
    tmp = ''
    for x in range(len(arr)):
        makeT(aToh(arr[x]))
    print('#{} {}'.format(k + 1, tmp))
