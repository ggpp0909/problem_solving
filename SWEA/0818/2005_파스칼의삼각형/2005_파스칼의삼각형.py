import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())

dp = [0 for i in range(1010)]   # 메모이제이션을 위한 배열

def pascal(n):   # 파스칼 삼각형의 n번째 줄을 리스트로 리턴하는 함수
    if dp[n]:    # 값이 구해져 있으면 그냥 써
        return dp[n]

    if n == 1:
        dp[n] = [1]
        return dp[n]

    if n == 2:
        dp[n] = [1, 1]
        return dp[n]

    if n > 2:   # 값이 구해져 있지 않으면 만들어서 저장하고 리턴 해
        temp = pascal(n - 1)
        arr = []
        for i in range(1, len(temp)):
            arr.append(temp[i - 1] + temp[i])

        dp[n] = [1] + arr + [1]
        return dp[n]

for k in range(1, n+1):
    a = int(input())
    print('#{}'.format(k))
    for i in range(1, a+1):
        print(*pascal(i))
