import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
poke = []
pokedic = {}
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    poke.append(temp)
    pokedic[temp] = i + 1


for i in range(m):
    temp = sys.stdin.readline().rstrip()
    if temp.isdigit():
        print(poke[int(temp) - 1])
    else:
        print(pokedic[temp])

