m,n = map(int,input().split())

arr=[0]*1010

def recur (cur,start):
    if cur == n:
        for i in range(n):
            print(arr[i],end=" ")
        print("")
        return

    for i in range(start,m):
        arr[cur]=i+1
        recur(cur + 1 , i +1)

recur(0,0)
