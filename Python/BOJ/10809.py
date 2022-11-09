alpha = 'abcdefghijklmnopqrstuvwxyz'
a=input()
lst = [-1 for i in range(26)]
for i in range(len(a)):
    if lst[alpha.index(a[i])] != -1:
        pass
    else:
        lst[alpha.index(a[i])]=i

for i in range(len(lst)):
    print(lst[i],end=" ")
