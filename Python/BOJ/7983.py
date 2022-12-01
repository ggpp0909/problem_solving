import sys
input = sys.stdin.readline

n = int(input())
# 쿼리를 끝나는 날 기준으로 내림차순 정렬, 끝나는 날부터 걸리는 날까지 차곡차곡 쌓기
# 스택의 top이 다음 쿼리의 끝일을 넘어서면 그 이후부터 차곡차곡 쌓기

arr = [list(map(int, input().split())) for i in range(n)]
arr.sort(key=lambda x: -x[1])
# print(arr)
stack = [99999999999]
for i in arr:
    cnt, end_day = i
    if stack[-1] >= end_day:
        stack.append(end_day - cnt)
    else:
        stack.append(stack[-1] - cnt)

print(stack[-1])
