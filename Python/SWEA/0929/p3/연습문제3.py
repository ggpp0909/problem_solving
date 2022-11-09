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

pw = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}

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
for _ in range(tc):
    arr = input()
    tmp = ''
    for x in range(len(arr)):
        makeT(aToh(arr[x]))
    temp = tmp[::-1]

    password = []
    for i in range(len(temp)):
        if temp[i] == '1':
            init = i
            while temp[init] == '1':
                password.append(temp[init:init+6][::-1])
                init += 6
            break
    password = password[::-1]
    for i in password:
        print(pw[i], end=' ')
    print()