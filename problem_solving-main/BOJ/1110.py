N=int(input())
cycle=0
a=N
while True:
    a=(a%10)*10 + ((a//10)+(a%10))%10
    cycle+=1

    if a==N:
        print(cycle)
        break
