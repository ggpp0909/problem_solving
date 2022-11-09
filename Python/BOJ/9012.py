N=int(input())
for _ in range(N):
    b=input() #입력받아
    index=0             #초기화
    status = True
    for i in range(len(b)): # b한글자씩스캔할거야
        if b[i]=="(":
            index+=1
        elif b[i]==")":
            index-=1
            if index<0:     #index가 0에서 닫는괄호로 시작하면 안됨
                status=False
                break
    if (status == False) or (index != 0): #다 스캔했을때 index가 0이 아니면 () 짝이 안맞는거
        print("NO")
    else:       #아무이상없으면 YES
        print("YES")
