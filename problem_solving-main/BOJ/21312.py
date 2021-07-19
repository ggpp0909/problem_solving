a, b, c = map(int,input().split())
if a%2==0 and b%2==0 and c%2==0:
    ans=a*b*c
else:
    if a%2==0:
        a=1
    if b%2==0:
        b=1
    if c%2==0:
        c=1
    ans=a*b*c
print(ans)
