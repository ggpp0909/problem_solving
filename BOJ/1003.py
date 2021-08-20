def fibo(n):
    global call0, call1
    if n == 0:
        call0 += 1
    elif n == 1:
        call1 += 1
    else:
        if dp[n]:
            call0 += dp[n][0]
            call1 += dp[n][1]
        else:
            fibo(n-1)
            fibo(n-2)
            dp[n] = [call0, call1]
        
dp = [0 for i in range(50)]

n = int(input())
for i in range(n):
    call0 = 0
    call1 = 0
    a = int(input())
    fibo(a)
    print(call0,call1)
