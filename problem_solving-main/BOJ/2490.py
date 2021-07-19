ans_list=[]

for _ in range(3):
    N =input().split()
    for i in range(len(N)):
        N[i] = int(N[i])
        
    if N.count(0)==0:
        ans="E"
    elif N.count(0)==1:
        ans="A"
    elif N.count(0)==2:
        ans="B"
    elif N.count(0)==3:
        ans="C"
    elif N.count(0)==4:
        ans="D"
    ans_list.append(ans)

for i in range(len(ans_list)):
    print(ans_list[i])
