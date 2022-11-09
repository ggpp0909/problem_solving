def effort(a,b):
    x=[1,0,1,2,0,1,2,0,1,2]
    y=[3,0,0,0,1,1,1,2,2,2]
    eff=abs(x[a]-x[b])+abs(y[a]-y[b])
    return eff

time=input()
hour=int(time[0:2])
ans=100 #걍아무거나 큰수

while hour<100:
    min=int(time[3:5])
    while min < 100:
         #에포트 구하기
        eff = effort(hour//10, hour%10) + effort(hour%10,min//10) + effort(min//10,min%10)
        if eff <ans:
            ans=eff
            ans_hour = hour
            ans_min = min  #최소 에포트 받을때마다 업데이트
        min += 60
          #min에 60더하기
    hour += 24

if ans_hour//10==0: #한자리수인경우 0붙여서 출력
    ans_hour="0"+str(ans_hour)
if ans_min//10==0:
    ans_min="0"+str(ans_min)

print(str(ans_hour)+":"+str(ans_min))
    
