import sys
sys.stdin = open('input.txt')

T = int(input())

for k in range(1, T + 1):
    d, m, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    dp = [0 for i in range(13)]

    for i in range(1, 13): # 세달째부터
        d_fee = dp[i - 1] + d * month[i] # 이거때문에 그 달 이용안하면 자동으로 dp[i]는 d_fee인 dp[i-1]로 됨
        m_fee = dp[i - 1] + m
        m3_fee = dp[i - 3] + m3     # 조건 알걸어줘도 dp[음수](끝인덱스)가 처음에 0이기 때문에 그대로해도 됨

        dp[i] = min(d_fee, m_fee, m3_fee)

    ans = min(dp[12], y) # 마지막 1년이용권과 비교

    print('#{} {}'.format(k, ans))
