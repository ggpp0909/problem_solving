def fibo(n):
    if dp[n]:
        return dp[n]
    else:
        if n==1 or n==2 or n==3:
            dp[n]=1
        else:
            dp[n] = fibo(n-1) + fibo(n-3)
        return dp[n]

n = int(input())
dp = [0 for i in range(n + 10)]
print(fibo(n))
