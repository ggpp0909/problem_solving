n=int(input())
dp=[None for i in range(n+10)]

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    if dp[n] != None:
        return dp[n]

    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

print(fibo(n))
