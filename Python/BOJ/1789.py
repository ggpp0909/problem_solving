n = int(input())

tot = 0
for i in range(1,1000000000):
    tot += i
    if tot > n:
        print(i-1)
        break