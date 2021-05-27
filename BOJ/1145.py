a= input().split()
for i in range(len(a)):
    a[i] = int(a[i])


for i in range(1,999999999): #완전탐색
    cnt=0
    for k in a:
        if i % k ==0:
            cnt+=1
    
    if cnt>=3:
        ans=i
        break

print(ans)   
