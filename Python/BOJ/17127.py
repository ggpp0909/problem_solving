N=int(input())
a=input().split()
for i in range(len(a)):
    a[i] = int(a[i])
ans=0

def multiply(x):
    temp=1
    for i in x:
        temp*= i
    return temp



for i in range(1,N):
    for j in range(1,N):
        for k in range(1,N):
            for l in range(1,N):
                if i+j+k+l==N:
                    temp=multiply(a[:i])+multiply(a[i:i+j])+multiply(a[i+j:i+j+k]) + multiply(a[i+j+k:i+j+k+l])
                    if temp>ans:
                        ans=temp

print(ans)
