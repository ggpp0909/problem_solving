N=int(input())

a= input().split()

for i in range(len(a)):
    a[i] = int(a[i])

cnt= 0
for i in a:
    status=0
    for k in range(2,i+1):
        if i%k==0 :
            status+=1
    if status == 1:
        cnt +=1

print(cnt)
