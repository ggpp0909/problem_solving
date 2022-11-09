a, b = map(int,input().split())

def GCD(a,b):
    while a %b!=0:
        temp=a%b
        a=b
        b=temp
    return b

x= b//a
lst=[]
for i in range(1,x+1):
    if i*i>x:
        break
    
    if x%i==0:
        lst.append(i)

for i in range(len(lst)-1,-1,-1):
    if GCD(lst[i],x//lst[i])==1:
        print(lst[i]*a,(x//lst[i])*a)
        break
        
    

