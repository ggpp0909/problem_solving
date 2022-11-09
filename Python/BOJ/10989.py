import sys

N=int(sys.stdin.readline())
lst=[0]*10001

for _ in range(N):
    a=int(sys.stdin.readline())
    lst[a-1] +=1
cnt=0
for i in range(len(lst)):
    cnt+=1
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(cnt)
