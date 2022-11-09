import sys
N = int(sys.stdin.readline())
for k in range(N):
    a= sys.stdin.readline().split()
    c=0
    for i in range(len(a)):
        a[i]=int(a[i])
        c+=a[i]
    print(c)
