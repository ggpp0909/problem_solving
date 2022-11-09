n,m = map(int,input().split())
lst=[0] * 100           #m자릿수

def Ing_gimoring(cur):
    if cur == m:
        for i in range(m):
            print(lst[i], end=' ')
        print("")
        return

    for i in range(1,n+1):
        lst[cur] = i
        Ing_gimoring(cur + 1)

Ing_gimoring(0)
