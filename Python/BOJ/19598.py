# 아이디어 1
# 아이모스 마냥 쿼리의 끝만 찍어놓고 O(n)에 처리
# -> 배열 크기 2 ** 31 이므로 시간초과 날듯

# 아이디어 2 괄호 맞추기(스택) 문제마냥 접근
# 1~ 10 이랑  5 ~ 15의 겹치는 구간은 5~10 즉 1~15와 5~10랑 동치,
# 오름차순 정렬, 최대 괄호 뎁쓰구하기
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    l, r = map(int, input().split())
    # 0 왼쪽
    arr.append([l, 0])
    arr.append([r, 1])

# 오름차순 정렬
arr.sort(key=lambda x: (x[0], -x[1])) # 이렇게한 이유는 같은시간대에 시작, 끝 겹치는 반례때문
# print(arr)

ans = 0
cascade = 0
for i in range(len(arr)):
    if arr[i][1] == 0:
        cascade += 1
        ans = max(ans, cascade)
    else:
        cascade -= 1
print(ans)
