N=int(input())
a=input().split()

for i in range(len(a)):
    a[i]=int(a[i])

a.sort()
ans=0
for i in range(len(a)):
    ans+=a[i]*(len(a)-i)

print(ans)
