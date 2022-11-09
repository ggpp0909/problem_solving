lst=["c=","c-","dz=","d-","lj","nj","s=","z="]
a=input()

for i in lst:
    a=a.replace(i,"_")


print(len(a))
