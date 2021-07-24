import sys
A, B, C = map(int, sys.stdin.readline().split())

i = 0

while True:
    if B >= C:
        print(-1)
        break

    i += 1
    rev = C * i - (A + B * i)
    
    if rev > 0:
        print(i)
        break
