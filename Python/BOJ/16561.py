N= int(input())
ans=1
cnt=2
for i in range(9,N,3):
    ans=ans+cnt
    cnt+=1

print(ans)
