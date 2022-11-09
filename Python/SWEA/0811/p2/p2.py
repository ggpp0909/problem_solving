import sys
sys.stdin = open('input.txt')

n = int(input())
for k in range(1, n + 1):
    arr = list(map(int, input().split()))
    ans = 0

    def recur(cur = 0, tot = 0, cnt = 0):  # 재귀깊이, 부분집합의 합, 원소개수
        global ans
        if cur == 10:  # 기저까지 들어왔어?
            if tot == 0 and cnt != 0:  # 판별
                ans = 1
            return

        # 원소를 포함할경우
        recur(cur + 1, tot + arr[cur], cnt + 1)
        # 원소를 포함하지 않을경우
        recur(cur + 1, tot, cnt)

    recur()
    print('#{} {}'.format(k, ans))


# 한 state에서 두가지의 상황으로 분리하여 재귀호출을 함
# 두가지의 상황 -> 원소를 포함한다. or 안한다.
# 호출하면서 한단계 더 깊이 들어가므로 cur + 1
# cur은 동시에 arr의 인덱스에 매칭됨
# cnt는 공집합 처리를 위해 선언