N= int(input())

lst=[]
for i in range(N):
    a=int(input())
    lst.append(a)

lst=sorted(lst)
for i in lst:
    print(i)

