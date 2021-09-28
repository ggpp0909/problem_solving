import sys
sys.stdin = open('input.txt')

n = int(input())
for k in range(1, n+1):
    print(input()[::-1])
