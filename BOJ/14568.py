input=int(input())
cnt=0

for T in range(1,input+1):
    for Y in range(1, input+1 -T):
        for N in range(1, input+1 -T -Y):
            if (Y+N+T == input) and (T%2 != 1) and(N>=Y+2):
                 cnt += 1

print(cnt)
