N = input()
N= N[::-1]
A="-\(@?>&%"
ans=0
ans_list=[]
while N != "#":
    for i in range(len(N)):
        if N[i] == "/":
            ans= ans-(8**i)
        else:
            ans= ans + A.index(N[i]) * (8**i)

    ans_list.append(ans)
    ans=0
    N=input()
    N=N[::-1]

for i in range(len(ans_list)):
    print(ans_list[i])
