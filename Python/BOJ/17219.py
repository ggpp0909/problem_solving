import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dic = {}
for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    dic[a] = b

for i in range(m):
    print(dic[sys.stdin.readline().rstrip()])
