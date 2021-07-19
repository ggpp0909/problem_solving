N=input()
A=[]

for i in range(8):
    A.append(0)

for i in range(len(N)):
    if N[i] in "1QAZ":
        A[0] +=1
    elif N[i] in "2WSX":  
        A[1] +=1
    elif N[i] in "3EDC":  
        A[2] +=1
    elif N[i] in "4RFV5TGB":  
        A[3] +=1
    elif N[i] in "67YUHJNM":  
        A[4] +=1
    elif N[i] in "8IK,":  
        A[5] +=1
    elif N[i] in "9OL.":  
        A[6] +=1
    elif N[i] in "0-=P[];'/":  
        A[7] +=1

for i in range(8):
    print(A[i])
