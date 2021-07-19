N= input()
A=N
inspect= "CAMBRIDGE"

for i in range(len(N)):
    if N[i] in inspect:
        A=A.replace(N[i],"")

if (3<=len(N)<=100) and len(A)>=1:
    print(A)
