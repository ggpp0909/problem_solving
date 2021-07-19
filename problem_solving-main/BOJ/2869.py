import sys
import math

a,b,c = map(int,sys.stdin.readline().split())
cnt= (c-b)/(a-b)

print(math.ceil(cnt))
