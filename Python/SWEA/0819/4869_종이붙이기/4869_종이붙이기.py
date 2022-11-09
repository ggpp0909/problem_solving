import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

dp = [0 for i in range(100)]  # 그냥 다 채워놓고 꺼내 써
dp[1] = 1
dp[2] = 3
# 맨 앞에 놓을수 있는 타일의 모양은 3가지, 결국 이전에 구해놓은 3가지 경우를 더한경우가 dp[i]가됨
for i in range(3, len(dp)):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2])

for k in range(1, n + 1):
    w = int(input()) // 10
    print('#{} {}'.format(k, dp[w]))
