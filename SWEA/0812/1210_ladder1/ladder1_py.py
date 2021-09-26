import sys
sys.stdin = open('input.txt')

for k in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]  # 사다리

    idx = 0
    for i in range(100):  # 마지막 2를찾아
        if arr[99][i] == 2:
            idx = i

    for i in range(99, -1, -1):  # 거꾸로 올라가
        if idx > 0 and arr[i][idx - 1]:  # 인덱스 에러 방지용 벽 조건, 왼쪽에 길이있으면 왼쪽으로 쭉 달려
            while idx > 0 and arr[i][idx - 1]:
                idx -= 1
        elif idx < 99 and arr[i][idx + 1]:  # 오른쪽에 길을 찾으면 달려
            while idx < 99 and arr[i][idx + 1]:
                idx += 1

    print('#{} {}'.format(k, idx))

    # 손순철님 풀이 참고하였습니다





