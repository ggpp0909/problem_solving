import sys
sys.stdin = open('input.txt')

visited = [False for i in range(10)]

def baby_gin():
    global flag
    check = 0

    # 연속하는 숫자 3개가 모두 같은경우
    if arr[0] == arr[1] and arr[1] == arr[2]:
        check += 1
    if arr[3] == arr[4] and arr[4] == arr[5]:
        check += 1

    #연속하는 세자리수
    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
        check += 1
    if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]:
        check += 1

    if check == 2:
        flag = 1
        return

def perm(start, end):
    if start == end:
        baby_gin()
    else:
        for i in range(start, end):
            arr[end], arr[i] - arr[i], arr[end]
            perm(start + 1, end)
            arr[end], arr[i] = arr[i], arr[end]


for _ in range(int(input())):
    arr = list(map(int, input()))
    flag = 0
    perm(0, len(arr) - 1)

    if flag:
        print('True')
    else:
        print('False')