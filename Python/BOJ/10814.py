N=int(input())
lst=[]

for i in range(N):
    age, name = map(str,input().split())
    age=int(age)
    lst.append((age,name,i))

lst.sort(key= lambda x : (x[0],x[2]))

for i in range(N):
    print(lst[i][0],lst[i][1])
