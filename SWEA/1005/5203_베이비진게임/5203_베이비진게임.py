import sys
sys.stdin = open('input.txt')

def check(lst, n):
    global flag
    if lst[n] == 3:
        return True

    temp = [0, 0] + lst + [0, 0] # 인덱스에러 방지용, n의 인덱스 +2
    for i in range(3):  # n번째 인덱스 기준으로 완탐해서 triplet 찾아
        if temp[n + i] and temp[n + 1 + i] and temp[n + 2 + i]:
            return True

    return False    # 뭐든 걸렸으면 True 리턴, 아니면 False 리턴

T = int(input())

for k in range(1, T + 1):
    arr = list(map(int, input().split()))
    p1 = [0 for i in range(11)]
    p2 = [0 for i in range(11)]
    ans = 0

    for i in range(len(arr)):
        if i % 2:   # 0부터시작, 짝수라면? p2
            p2[arr[i]] += 1
            if check(p2, arr[i]):   # 뭐 걸린게 있어? 그럼 ans에 답저장해
                ans = 2
                break
        else:
            p1[arr[i]] += 1
            if check(p1, arr[i]):
                ans = 1
                break
    print('#{} {}'.format(k, ans))