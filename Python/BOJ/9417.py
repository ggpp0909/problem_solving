N=int(input())

for _ in range(N):
    a=input().split()
    ans=0
    for i in range(len(a)):
        a[i]=int(a[i])

    for i in range(len(a)):
        for k in range(len(a)):
            if i>=k:
                continue
            z = a[i]
            zz = a[k]
            while z%zz!=0:
                temp = z%zz
                z=zz
                zz=temp

            if zz>ans:
                ans=zz

    print(ans)
