s = input()
t = input()

dp = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]

for i in range(1, len(t) + 1):
    for j in range(1, len(s) + 1):
        if t[i - 1] == s[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[-1][-1])

ans = ''
i = len(t) #행
j = len(s) #열

while i > 0 and j > 0:

    if dp[i][j] == dp[i - 1][j]:    # 위에서왔니? 왼쪽에서왔니? 대각선에서왔니?
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        ans = s[j - 1] + ans # 문자가 같은 경우 빼고는 LCS가 늘어나는 경우가 없음. 대각선에서 왔을때 늘어남
        i -= 1
        j -= 1


if dp[-1][-1]:
    print(ans)

