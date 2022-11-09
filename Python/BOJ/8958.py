N=int(input())

for _ in range(N):
    a=input()
    cnt=0
    cnt_2=0
    for i in range(len(a)):
        if a[i]=="O":
            cnt+=1
            cnt_2 += cnt
        elif a[i]=="X":
            cnt=0
    print(cnt_2)
