case=int(input())
for i in range(case):
    N=int(input())
    cnt=0

    while N!= 6174:
        a=N%10
        b=(N//10)%10
        c=(N//100)%10
        d=N//1000
        lst = []
        lst.append(a)
        lst.append(b)
        lst.append(c)
        lst.append(d)
        lst.sort(reverse=True)
        A = lst[0]*1000+lst[1]*100 + lst[2]*10 + lst[3]

        lst.sort()
        B = lst[0] * 1000 + lst[1] * 100 + lst[2] * 10 + lst[3]

        N= A-B
        cnt += 1

    print(cnt)
