a=int(input())
cnt=a
for k in range(a):
    N=input()
    lst=[]
    for i in range(len(N)):
        if N[i] not in lst :
            lst.append(N[i])

        else:
            if N[i] != lst[len(lst)-1]:
                cnt -= 1
                break
print(cnt)
