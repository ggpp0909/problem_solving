N = int(input())
ans=0
ans_list=[]
temp=[]

for i in range(N):
    case= input().split()
    for k in range(len(case)):
        case[k] = int(case[k])
    
    case.sort()

    if case[0]==case[1]:
        if case[0]==1:
            ans="Habb Yakk"
        elif case[0]==2:
            ans="Dobara"
        elif case[0]==3:
            ans="Dousa"
        elif case[0]==4:
            ans="Dorgy"
        elif case[0]==5:
            ans="Dabash"
        elif case[0]==6:
            ans="Dosh"

    elif case[0]==5 and case[1]==6:
        ans="Sheesh Beesh"
    
    else:
        for j in range(len(case)):
            if case[j]==6:
                temp.append("Sheesh")
            elif case[j]==5:
                temp.append("Bang")
            elif case[j]==4:
                temp.append("Ghar")
            elif case[j]==3:
                temp.append("Seh")
            elif case[j]==2:
                temp.append("Doh")
            elif case[j]==1:
                temp.append("Yakk")
        ans=temp[1]+" "+temp[0]
       
    ans_list.append(ans)
    ans=0
    temp=[]
        
for l in range(N):
    print("Case {0}: {1}".format(l+1,ans_list[l]))
