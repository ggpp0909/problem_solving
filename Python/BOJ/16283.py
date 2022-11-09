a, b, n, w = map(int,input().split())
count =0
Ans=0
for x in range(1,n):
    if 1<=a<=1000 and 1<=b<=1000 and 2<=w<=1000000:
        if a*x + b*(n-x) == w:
         count += 1
         Ans=x
         
if count ==1:
    print(Ans,n-Ans)
else:
    print(-1)
