import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

def is_pal(arr):  # M글자의 회문 존재여부 판단함수, 존재할경우 회문, 아닐경우 0리턴
    ans = 0
    global flag
    for i in range(len(arr)):
        for j in range(len(arr[i]) - M + 1):
            word = arr[i][j:j + M]
            if word == word[::-1]:
                ans = word
                flag = 1
                break
        if flag:
            break
    return ans


for k in range(1, n + 1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    flag = 0
    # 가로 탐색
    w = is_pal(arr)
    if w:
        print('#{} {}'.format(k, w))

    # 세로탐색
    if not flag:  # flag 가 1일경우 불필요한 연산 x
        temp = [''] * N
        for i in range(len(arr)):  #세로를 가로로 바꾸기
            for j in range(len(arr)):
                temp[j] += arr[i][j]

        print('#{} {}'.format(k, is_pal(temp)))
