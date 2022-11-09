import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(sys.stdin.readline().rstrip().split())

arr2 = []
for i in arr:
    if i[1] == 'enter':
        arr2.append(i[0])
    elif i[1] == 'leave':
        arr2.remove(i[0])

arr2.sort(reverse=True)
for i in arr2:
    print(i)
