import sys
sys.setrecursionlimit(200000)

n=int(sys.stdin.readline())
arr=[-1 for i in range(n +10)]

def sum_square(n):
   if arr[n] != -1: #값이 저장되어 있다면 저장된 값 리턴
      return arr[n]

   if int(n**(1/2))==n**(1/2): #제곱수라면 1 리턴
      arr[n]=1
      return arr[n]
   
   maxnum = 100010
   for i in range(1,n+1): #그 외 경우 dp[n-1], dp[n-4], dp[n-9] ... 중 최솟값 + 1
      if i*i>n:
         break
      if sum_square(n-i**2) < maxnum:
         maxnum = sum_square(n-i**2)
   arr[n] = maxnum + 1
   
   return arr[n]

print(sum_square(n))