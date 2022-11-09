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

def makeT(x):
    for i in range(4):
        tmp.append(asc[x][i])

def aToh(x):
    if x <= '9':
        return ord(x) - ord('0')
    else:
        return ord(x) - ord('0') - 7

tc = int(input())
for _ in range(tc):
    arr = input()
    tmp = []
    for x in range(len(arr)):
        makeT(aToh(arr[x]))


    result = 0
    for i in range(len(tmp)):
        result = result * 2 + tmp[i]
        if i % 7 == 6:
            print(result, end=' ')
            result = 0
    if i % 7 != 6:
        print(result)
