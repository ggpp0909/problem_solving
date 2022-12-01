import sys
input = sys.stdin.readline

# n = int(input())
# # 쿼리를 끝나는 날 기준으로 내림차순 정렬, 끝나는 날부터 걸리는 날까지 차곡차곡 쌓기
# # 스택의 top이 다음 쿼리의 끝일을 넘어서면 그 이후부터 차곡차곡 쌓기

# arr = [list(map(int, input().split())) for i in range(n)]
# arr.sort(key=lambda x: -x[1])
# # print(arr)
# stack = [99999999999]
# for i in arr:
#     cnt, end_day = i
#     if stack[-1] >= end_day:
#         stack.append(end_day - cnt)
#     else:
#         stack.append(stack[-1] - cnt)

# print(stack[-1])

n = int(input())
# 끝나는날 기준 내림차순 정렬후 시작일만 들고 한번 탐색하기
# 예를들면 지금이 10이였는데 이번일이 8일 마감이고 3일걸리면 답은 5
# 그게아니라 지금이 10인데 이번일이 15일까지고 마감이 3일걸리면 답은 7
# 즉 제일 빨리 시작해야 되는 날과 새로운 일의 마감일을 비교하면서 업데이트하기

arr = [list(map(int, input().split())) for i in range(n)]
arr.sort(key=lambda x: -x[1])

ans = 99999999999

for i in arr:
    cnt, end_day = i
    ans = min(ans, end_day) - cnt

print(ans)