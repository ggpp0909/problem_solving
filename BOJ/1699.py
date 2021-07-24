import sys

n= int(sys.stdin.readline())
dp=[0 for i in range(n+1)]

result = 0
for i in range(1,n+1):  
    lst=[]
    for j in range(1,i+1):
        if j**2>i:
            break
        lst.append(dp[i-j**2])
    dp [i]= min(lst)+1

print(dp[n])