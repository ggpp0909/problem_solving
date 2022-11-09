a,b = map(int,input().split())
A=[]

for x in list(range(-100,100,1)):
    if x*x + 2*a*x + b == 0:
        A.append(x)

A.sort()

for i in A:
    print(i, end=" ")
