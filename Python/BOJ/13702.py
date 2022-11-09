N ,K = map(int, input().split())

lst = []
for i in range(N):
    lst.append(int(input()))

s = 0
e = 10000000000

while s <= e:
    mid = (s + e) // 2
    
    tot=0
    for i in lst:
        tot += i // mid

    if K > tot:
        e = mid - 1

    elif K <= tot:
        ans = mid
        s = mid + 1
        
print(ans)