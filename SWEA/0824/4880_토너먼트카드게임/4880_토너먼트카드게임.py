import sys
sys.stdin = open('input.txt')

# 1 가위 2 바위 3 보
def winner(a, b): # a, b 가위바위보 했을때 이긴놈(인덱스) 반환
    if arr[a] == arr[b] or (arr[a] == 1 and arr[b] == 3) or (arr[a] == 2 and arr[b] == 1) or (arr[a] == 3 and arr[b] == 2):
        return a
    else:
        return b

def recur(s, e): # 배열의 끝인덱스, 시작인덱스
    if s == e:  # 한명이 될때까지
        return s

    mid = (s + e) // 2
    return winner(recur(s, mid), recur(mid + 1, e))

n = int(input())
for k in range(1, n + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(k, recur(0, len(arr) - 1) + 1))
