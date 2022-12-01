import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input()) # 10만

pb = defaultdict(int) # 기본값 0으로

for i in range(N):
    a, b = map(int, input().split())
    pb[a] = b


M = int(input()) # 1만

def add(pbnum, difficulty):
    pb[pbnum] = difficulty
    return

def recommend(x):
    if x == 1:
        pass
    elif x == -1:
        pass

    return

def solved(pbnum):
    pb[pbnum] = 0
    return

print(defaultdict.items())

for i in range(M):
    temp = input().split()
    if temp[0] == "add":
        add(int(temp[1]), int(temp[2]))
    elif temp[0] == "recommend":
        recommend(int(temp[1]))
    elif temp[0] == "solved":
        solved(int(temp[1]))