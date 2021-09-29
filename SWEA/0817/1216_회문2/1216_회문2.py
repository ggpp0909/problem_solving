import sys
sys.stdin = open('input.txt', encoding='UTF8')

def is_pal(arr):  # for문을 돌면서 가장 긴 회문이 나올때마다 회문의 길이를 ans에 저장
    global ans
    for i in range(100):
        for j in range(100):
            for k in range(j, 100):
                word = arr[i][j:k+1]
                if word == word[::-1]:
                    temp = len(word)
                    if ans < temp:
                        ans = temp
    return

for k in range(1, 11):
    n = int(input())
    arr = [input() for i in range(100)]
    ans = 0

    #세로(전치행렬)
    T = ['' for i in range(100)]
    for i in range(len(arr)):  #세로를 가로로 바꾸기
        for j in range(len(arr)):
            T[j] += arr[i][j]

    is_pal(arr)
    is_pal(T)
    print('#{} {}'.format(k, ans))
