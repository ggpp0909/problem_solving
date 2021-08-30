n = int(input())
for k in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = abs(complex(x1 - x2, y1 - y2))
    
    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif dis > r1 + r2:
        print(0)
    elif dis == r1 + r2:
        print(1)
    elif dis + min(r1, r2) == max(r1, r2):
        print(1)
    elif dis + min(r1, r2) < max(r1, r2):
        print(0)
    else:
        print(2)