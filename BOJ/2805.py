import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))


s = 0
e = 1000000000
while s <= e:
    mid = (s + e) // 2

    tot = 0
    for i in arr:
        if i - mid > 0:
            tot += i-mid
    
    if tot >= m: 
        s = mid + 1 #톱 높이를 높여
    
    else:
        e = mid - 1 #톱 높이를 줄여
    
print(e)