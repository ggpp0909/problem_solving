N= int(input())
dp= [-2 for i in range(5010)]
import sys
sys.setrecursionlimit(10**7)

#nkg의 설탕을 최소 몇봉지로 배달가능한지를 리턴할수 있는 함수

def recur(n):
    #종료조건
    if n==0:
        return 0
    elif n<0:
        return -1
    
    #메모이제이션
    if dp[n]!=-2:
        return dp[n]

    #재귀호출
    a=recur(n-3)
    b=recur(n-5)
    if a==-1 and b==-1:
        dp[n]=-1
    elif a==-1:
        dp[n]=b+1
    elif b==-1:
        dp[n]=a+1
    else:
        dp[n]=min(a,b)+1
    return dp[n]

print(recur(N))
