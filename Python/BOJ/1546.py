N=int(input())

a = input().split()
sum =0
for i in range(len(a)):
    a[i]= int(a[i])
    sum+=a[i]


M=max(a)


avg=((sum/M)*100)/N
print(avg)
