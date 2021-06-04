A, B= map(int,input().split())

for i in range (10000,0,-1):
    if A%i==0 and B%i==0:
        ans1=i
        break


ans2=(A*B)//ans1

print(ans1)
print(ans2)
