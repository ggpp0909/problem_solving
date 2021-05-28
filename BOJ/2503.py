N=int(input())
num_list=[]
s_list=[]
b_list=[]


for i in range(N):
    num,s,b=map(str,input().split()) #입력을 리스트에 쌓음
    num_list.append(num)
    s_list.append(s)
    b_list.append(b)

ans_cnt=0
for i in range(100,1000): #100~999완전탐색
    i=str(i)
    cnt=0
    if i[0] != i[1] and i[1] != i[2] and i[0] != i[2] and ('0' not in i): #각자리수가 달라야됨
        for k in range(N): #첫번째 입력부터 차례로 검사
            strike=0
            ball=0
            
            for j in range(3):#num의 자리수 하나씩 검사
                if num_list[k][j]== i[j]: #자릿수가 일치하면 스트라이크
                    strike +=1
                elif num_list[k][j] in i: #일치하진않지만 그숫자가 i에 들어가있으면 볼
                    ball +=1
                # print(strike,ball)
            if s_list[k]==str(strike) and b_list[k]==str(ball): #스트라이크와 볼이 맞으면 카운트
                cnt +=1
                
                
        if cnt==N: #만약 모든경우가 들어맞으면 카운트
            ans_cnt+=1
            
print(ans_cnt)
