lst =[]
for i in range(9):
    lst.append(int(input()))

all_sum=sum(lst)
k_l=[]
for i in range(len(lst)-1):
    for k in range(i+1,len(lst)):
        ans=all_sum-lst[i]-lst[k]
        if ans ==100:
            k_l.append(k)
            k_l.append(i)
            break
ans=[]

for i in lst:
    if i != lst[k_l[0]] and i != lst[k_l[1]]:
        ans.append(i)
ans.sort()
for i in ans:
    print(i,end= ' ')
