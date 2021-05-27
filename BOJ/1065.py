N=int(input())
ans=0
for i in range(1,N+1):
    cnt=0
    a=i//10
    while True: #N이 몇자리수인지 찾기
        cnt +=1
        if a==0:
            break
        a=a//10
    
    a=[]
    b=i
    c=i//10
    for _ in range(cnt): #자리수만큼 반복 각 자리수 a에 뽑아넣기
        b=b%10
        a.append(b)
        b=c
        c=c//10
    
    hansu=True
    for k in range(len(a)-2):#등차수열인지 검사
        if a[k+1]-a[k]!=a[k+2]-a[k+1]: #하나라도 공차가 다른경우 한수가아님
            hansu=False
    
    if hansu==True: #한수라면 카운트
        ans+=1

print(ans)
