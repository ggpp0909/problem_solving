N = int(input())
same=0
money=0
max_list=[]


for i in range(N):
    a,b,c = map(int,input().split())
    if a == b == c:
        same=a
    elif a==b or a==c:
        same = a
    elif b==c:
        same = b
    else:
        same=max(a,b,c)

    if a==b==c:
        money=same*1000 + 10000
    elif a==b or a==c or b==c:
        money=1000+same*100
    else:
        money=same*100
    
    max_list.append(money)

print(max(max_list)) 
