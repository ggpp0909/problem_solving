N, M, K = map(int,input().split())
count = K
while count>0:
    if N >= 2*M:
        N -=1
        count -=1
    elif N< 2*M:
        M -=1
        count -=1

if N > 2*M:
    print(M)
elif N<= 2*M:
    print(N//2)
